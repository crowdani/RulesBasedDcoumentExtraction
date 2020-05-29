import datetime as dt
from loggingHandler import logger
from downloadFiles import downloadFiles
from uploadFiles import uploadFiles
from deleteFiles import deleteFiles
from updateReport import updateReport
from executeRules import executeRules
from oauth import oauth

starttime = dt.datetime.now()



uploadSuccess = oauth()
bearerToken = "Bearer " + uploadSuccess
print(bearerToken)
