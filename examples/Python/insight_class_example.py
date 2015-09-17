from Insight import *
from arduinoCom import *

# -------------------------------------------------------------------------
# Make dictionary for logEmoState

header = ['Time', 'UserID', 'wirelessSigStatus', 'Blink', 'leftWink',
          'rightWink', 'Surprise', 'Frown',
          'Smile', 'Clench',
          'shortExcitement', 'longExcitement',
          'Boredom', 'MentalCommand Action', 'MentalCommand Power']
emoStateDict = {}
for emoState in header:
    emoStateDict.setdefault(emoState, None)

# # -------------------------------------------------------------------------
#
# # connect to Arduino
#
# print "==================================================================="
# print "Please enter port for Arduino"
# print "==================================================================="
# print "Example:"
# print "Mac -- \n /dev/tty.usbmodem1451 "
# print "Windows -- \n COM4"
# print ">>"
# arduino_port = str(raw_input())
# setupSerial(arduino_port)
# -------------------------------------------------------------------------
# start EmoEngine or EmoComposer

print "==================================================================="
print "Example to show how to log EmoState from EmoEngine/EmoComposer."
print "==================================================================="
print "Press '1' to start and connect to the EmoEngine                    "
print "Press '2' to connect to the EmoComposer                            "
print ">> "

log_from_emo = int(raw_input())
# -------------------------------------------------------------------------

# instantiate Insight class
if log_from_emo == 1:
    insight = Insight()
elif log_from_emo == 2:
    insight = Insight(composerConnect=True)
else:
    print "option = ?"

print "Start receiving Emostate! Press any key to stop logging...\n"

# connect insight instance to Xavier composer or EmoEngine
insight.connect()
while (1):
    # set of operations to get state from Insight
    # returns 0 if successful
    state = insight.get_state(insight.eEvent)
    if state== 0:
        # event types IEE_Event_t returns 64 if EmoStateUpdated
        eventType = insight.get_event_type(insight.eEvent)
        user_ID = insight.get_userID(insight.eEvent, insight.user)
        if eventType == 64:
            insight.get_engine_event_emo_state(insight.eEvent, insight.eState)
            timestamp = insight.get_time_from_start(insight.eState)
            print "%10.3f New EmoState from user %d ...\r" % (timestamp,
                                                              user_ID)
            print insight.get_wireless_signal_status(insight.eState)
    elif state != 0x0600:
        print "Internal error in Emotiv Engine ! "
    time.sleep(1)
