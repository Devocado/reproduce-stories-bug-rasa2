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
* create_shipment: Please help me ship some items
    - create_shipment_form
    - form{"name":"create_shipment_form"}
    - form{"name":null}
    - utter_confirm_shipping_details
    - utter_track_new_shipment

## Track shipment happy path
* greet: Hi
    - utter_greet
    - user_details_form
    - form{"name":"user_details_form"}
    - form{"name":null}
    - utter_how_can_help
* track_shipment: When will my parcel arrive?
    - utter_track_shipment

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