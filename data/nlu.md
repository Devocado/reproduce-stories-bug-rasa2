## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hi
- Hello
- heya

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- yes, please
- right
- yup
- that's right
- perfect

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- no, neither
- nope
- negative
- none of those

## intent:request_human
- please can I speak to a human
- I want a human
- Give me a person
- Please hand me over to a person
- I want to speak to a person

## intent:thanks
- thanks
- thank you
- great, thanks
- wow thanks
- thx
- thnx

## intent:inform_address
- [23](number) flower street, Leeds
- [111](number) Signal Road, Chester
- [28](number) Heron Crescent, Eastlake Estate, Montague
- Lonely house, [57](number) Cherry Lane, East March

## intent:inform_number_items
- [1](number)
- I want to ship [12](number) parcels
- [one]{"entity":"number","value":"1"}
- [two]{"entity":"number","value":"2"}
- [three]{"entity":"number","value":"3"}
- [four]{"entity":"number","value":"4"}
- [five]{"entity":"number","value":"5"}
- [six]{"entity":"number","value":"6"}
- [seven]{"entity":"number","value":"7"}
- [eight]{"entity":"number","value":"8"}
- [nine]{"entity":"number","value":"9"}
- [ten]{"entity":"number","value":"10"}
- [eleven]{"entity":"number","value":"11"}
- [twelve]{"entity":"number","value":"12"}
- [thirteen]{"entity":"number","value":"13"}
- [fourteen]{"entity":"number","value":"14"}
- [fifteen]{"entity":"number","value":"15"}
- [sixteen]{"entity":"number","value":"16"}
- [seventeen]{"entity":"number","value":"17"}
- [eighteen]{"entity":"number","value":"18"}
- [nineteen]{"entity":"number","value":"19"}

## intent:track_shipment
- Where is my delivery
- how long will it take for my parcel to get here
- how much longer will it take
- when is my shipment coming?
- eta for my shipment?

## intent:create_shipment
- I want to ship an item
- I want to send something
- how do I ship an item with you
- I want to send a parcel
- I have an item to ship
- How do I get something delivered to me?
- make a new shipment
- I want to make another shipment
- send a parcel
- please help me ship items

## intent:inform_email
- [test@examplemail.com](email)
- my email is [x@mydomain.co.za](email)
- here is my email: [peter@russian.com](email)
- email address is [some.randomtext@nothing.ru](email)
- [happyday.allwelcome@hotmail.com](email)
- [mymushroomfarm@gmail.com](email) is my address
- my address is [bigfoot44@yahoo.com](email)
- [sharon@smith.co.za](email)
- my email is [streetwise+323@432.53.co.za](email)
- [32mike432@385.8.32.ru](email)

## intent:out_of_scope
- Please send me my latest invoice
- I have a complaint
- How much does your service cost?
- Where do you deliver to?

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## regex:email
- ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
