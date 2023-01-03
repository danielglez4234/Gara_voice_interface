# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import datetime as dt
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SessionStarted, ActionExecuted

# After adding this action to your domain file, 
# re-train your model with rasa train --force. Otherwise 
# Rasa won't know you've changed anything and may skip 
# re-training your dialogue model.
# command: train --force && run --enable-api --cors "*" --port 5045

# CollectingDispatcher -> send messages back to the user
# Tracker -> Fetch information: contains relevent data that was strac for the conversation so far (Intent, Entities, Conversation, Sofar)
# Domain -> access to data defain on yaml file (domain.yml)

class ActionShowTime(Action):
    def name(self) -> Text:
        return "action_show_time"
    
    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{dt.datetime.now()}")
        return []


class ActionTestActions(Action):
    def name(self) -> Text:
        return "action_test_actions"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(text="Testing...")
        print("Testing...")
        return []


class SessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        metadata = tracker.get_slot("session_started_metadata")

        # Do something with the metadata
        print(metadata)

        # the session should begin with a `session_started` event and an `action_listen`
        # as a user message follows
        return [SessionStarted(), ActionExecuted("action_listen")]


class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_nlu_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="I couldnt understand you")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(tracker)
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionPresentation(Action):
    
    def name(self) -> Text:
        return "action_presentation"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="it works")
        
        return []