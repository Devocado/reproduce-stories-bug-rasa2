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

## Create email no setup
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

## Not email query handoff
* greet
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* deny
    - utter_human_handoff

## Request human handoff interrupt form
* greet
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* create_shipment
    - create_shipment_form
    - form{"name":"create_shipment_form"}
* request_human
    - form{"name":null}
    - utter_human_handoff

## Thanks
* thanks
    - utter_my_pleasure

## out of scope
* out_of_scope
    - utter_out_of_scope
* affirm
    - utter_human_handoff

## out of scope no human
* out_of_scope
    - utter_out_of_scope
* deny
    - utter_anything_else
* affirm
    - utter_how_can_help

## out of scope loop handoff
* out_of_scope
    - utter_out_of_scope
* deny
    - utter_anything_else
* deny
    - utter_okay

## request human
* request_human
    - utter_human_handoff