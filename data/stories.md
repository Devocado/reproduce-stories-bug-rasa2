## Collect details happy path
* greet
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help

## Ship item happy path
* greet
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* create_shipment
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment

## Ship and track shipment
* greet
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* create_shipment
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment
* affirm
    - utter_track_shipment

## Ship and don't track want something else
* greet
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* create_shipment
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment
* deny
    - utter_anything_else
* affirm
    - utter_how_can_help

## track shipment
* track_shipment
    - utter_track_shipment

## Create email and ask setup
* greet
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* create_shipment
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment
* track_shipment
    - utter_track_shipment