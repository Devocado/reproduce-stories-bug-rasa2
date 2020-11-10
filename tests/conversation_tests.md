## Create shipment no track
* greet: Hello there!
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name": null}
    - utter_how_can_help
* create_shipment: Please help me ship some items
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment
* deny: No
    - utter_anything_else
* affirm: Yes
    - utter_how_can_help
* create_shipment: I want to create another shipment
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment

## Ship and track shipment
* greet: HI
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* create_shipment: I want to ship a parcel
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment
* affirm: yes
    - utter_track_shipment

## Create shipment no track
* greet: Hello there!
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name": null}
    - utter_how_can_help
* create_shipment: I want to ship a parcel
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment
* deny: No
    - utter_anything_else

## Track shipment happy path
* greet: Hi
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* track_shipment: When will my parcel arrive?
    - utter_track_shipment
* thanks: That's great, thanks!
    - utter_my_pleasure

## Not track or create shipment
* greet: Hello
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* deny: I don't want either of those
    - utter_human_handoff

## Out of scope want other help
* greet: Hello
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* out_of_scope: Where do you deliver?
    - utter_out_of_scope
* deny: no
    - utter_anything_else

## Out of scope want other help alternate
* greet: Hello
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* out_of_scope: Please sent me my latest invoice
    - utter_out_of_scope
* deny: no
    - utter_anything_else
* affirm: yes
    - utter_how_can_help

## Ask for human
* greet: Hello
    - utter_greet
    - user_details_form
    - form{"name":null}
    - utter_how_can_help
* request_human: Please can I speak to a human?
    - utter_human_handoff