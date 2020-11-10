# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.forms import FormAction

class UserDetailsForm(FormAction):
    def name(self) -> Text:
        return "user_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["client_name", "client_email"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(template = "utter_confirm_user_details", **tracker.slots)

        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "client_name": self.from_text(intent=None),
            "client_email": self.from_entity(entity="email", intent="inform_email")
        }

class ShipItemForm(FormAction):
    def name(self) -> Text:
        return "create_shipment_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["number_items", "from_address", "to_address"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "number_items": self.from_entity(entity="number", intent="inform_number_items"),
            "from_address": self.from_text(intent="inform_address"),
            "to_address": self.from_text(intent="inform_address"),
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        return []

class DefaultFallbackActionOverride(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_fallback")

        return []