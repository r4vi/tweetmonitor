from daemon import Daemon
from tweetstream import FilterStream, ConnectionError
import ConfigParser, os, sys
import couchdbkit
import logging, logging.handlers

config = ConfigParser.ConfigParser()
config.read('./settings.ini')
USER = config.get('tweetmonitor', 'user')
PASS = config.get('tweetmonitor', 'password')
COUCHDB_URI = config.get('tweetmonitor', 'couchdb_server')
words = [config.get('tweetmonitor', 'track')]



class Tweetmonitor(Daemon):
    def run(self):
        logFile = '/tmp/tweetmonitor.log'
        handler = logging.handlers.RotatingFileHandler(logFile, maxBytes=5485760, backupCount=3) # 10MB files
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        mainLogger = logging.getLogger('main')
        mainLogger.setLevel(logging.DEBUG)
        mainLogger.addHandler(handler)

        mainLogger.info('--')
        mainLogger.info('Tweetmonitor started')
        mainLogger.info('--')

        server = couchdbkit.Server(uri=COUCHDB_URI)
        db = server.get_or_create_db('tweetmonitor')

        try:
            with FilterStream(USER, PASS, track=words) as stream:
                for tweet in stream:
                    db.save_doc(tweet)
                    mainLogger.info("Got tweet from %-16s\t( tweet %d, rate %.1f tweets/sec)" % (
                    tweet["user"]["screen_name"], stream.count, stream.rate ))
        except ConnectionError, e:
            mainLogger.error("Disconnected from twitter. Reason: %s", e.reason)
            sys.exit(1)
