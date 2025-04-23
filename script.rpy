#definerer karakterer
define isak = Character("Isak", color="#ff8282")
define viggo = Character("Viggo", color="#42dff0")
define tobias = Character("Tobias", color="#dbff63")
define manager = Character("Manager", color="#282f70ff")

#definerer karaterbilder
image isak normal = "isakNormal.png"
image viggo normal = "viggoNormal.png"
image tobias normal = "tobiasNormal.png"
image manager normal = "managerAngry.png"
image manager angry = "managerAngry.png"

#defines scenes
image bakery_day = "menybakeri.png"
image bakery_outside ="menyUte.png"

label start:
    scene bakery_day with fade
    show tobias normal at center
    show isak normal at left
    show viggo normal at right

    voice "starttobiasline1.ogg"
    tobias "Alright, boys. Time for my usual deal. They don’t know it, but I’ve got it all figured out! They won't ever see it coming."

    voice "starttobiasline2.ogg"
    tobias "hehe."

    voice "startnarratorline1.ogg"
    "*Tobias heads to the self-checkout counter, his usual confident stride making the others a bit wary. Isak eyes him, but says nothing.*"


    hide tobias
    show isak normal at center

    voice "startisakline1.ogg"
    isak "You sure you want to do this again, Tobias? I don’t like the way this feels. You know it's like..."

    voice "startisakline2.ogg"
    isak "Illegal and stuff."


    hide isak
    show viggo normal at right

    voice "startviggoline1.ogg"
    viggo "Come on, Isak. It’s just buns. They’ll never know."

    voice "startviggoline2.ogg"
    viggo "Besides, it’s not like they’re going to miss a few pastries."


    hide viggo
    show tobias normal at center

    voice "startnarratorline2.ogg"
    "*Tobias grabs four pastries and scans one. He quickly slips the other three into his bag, his grin widening as he finishes scanning the one pastry.*"


    voice "starttobiasline3.ogg"
    tobias "I’m telling you, this is genius. Four buns for the price of one, and no one even notices."

    voice "starttobiasline4.ogg"
    tobias "It's like they’re giving them away!"

    voice "starttobiasline5.ogg"
    tobias "I wonder why no one else has thought of this before."


    hide tobias
    show isak normal at left

    voice "startisakline3.ogg"
    isak "Tobias, this isn’t just about getting a deal. You’re *stealing*. You’re better than this."

    voice "startisakline4.ogg"
    isak "There are consequences when stealing. Don't you understand?"


    hide isak
    show tobias normal at center

    voice "startnarratorline3.ogg"
    "*Tobias hesitates, the words hitting him harder than he expected. He pauses for a moment, glancing at the pastries in his bag.*"

    voice "starttobiasline6.ogg"
    tobias "I’m not stealing! I’m... I’m just getting what’s owed to me. They should have put up a sign or something, right?"

    voice "starttobiasline7.ogg"
    tobias "Everyone knows the 4 for 1 deal."

    voice "starttobiasline8.ogg"
    tobias "How can it be stealing if they're the one offering it?"


    hide tobias
    show viggo normal at right

    voice "startviggoline3.ogg"
    viggo "It’s fine. Don’t overthink it, man."

    voice "startviggoline4.ogg"
    viggo "They won’t ever notice, you’re just using the system to your advantage."


    hide viggo
    show isak normal at left

    voice "startisakline5.ogg"
    isak "I just don’t want to see you ruin yourself over this, Tobias."

    menu:
        "Tobias gives in and keeps walking out with the stolen pastries":
            $ tobias_stop = False
            jump bakery_confrontation
        "Tobias hesitates and gives the pastries back":
            $ tobias_stop = True
            jump bakery_return



label bakery_week_later:


    scene bakery_day with fade

    show tobias normal at center

    voice "starttobiasline9.ogg"
    tobias "This is easy money."

    voice "starttobiasline10.ogg"
    tobias "I can’t stop now."

    voice "starttobiasline11.ogg"
    tobias "Just four buns... it’s harmless."

    voice "startnarratorline4.ogg"
    "*Tobias grabs four pastries once again, scanning one, and quietly slipping the other three into his bag.*"

    voice "startnarratorline5.ogg"
    "*Isak watches him, arms crossed. Viggo seems more amused than concerned.*"


    hide tobias

    show isak normal at left

    voice "startisakline6.ogg"
    isak "Tobias, seriously."

    voice "startisakline7.ogg"
    isak "This isn’t how you solve things."

    voice "startisakline8.ogg"
    isak "This is going to catch up to you."

    voice "startisakline9.ogg"
    isak "It’s going to ruin everything."


    hide isak

    show tobias normal at center

    voice "startnarratorline6.ogg"
    "*Tobias scans the first pastry, trying to ignore Isak’s words.*"

    voice "startnarratorline7.ogg"
    "*But they linger.*"

    voice "startnarratorline8.ogg"
    "*He looks over at the others, unsure.*"

    voice "starttobiasline9.ogg"
    tobias "I don’t know, Isak..."

    voice "starttobiasline10.ogg"
    tobias "I’m just... making sure I get what’s mine."

    voice "starttobiasline11.ogg"
    tobias "You know? I’ve been coming here forever."


    hide tobias

    show viggo normal at right

    voice "startviggoline5.ogg"
    viggo "Who cares?"

    voice "startviggoline6.ogg"
    viggo "They won’t miss a couple of extra buns."

    voice "startviggoline7.ogg"
    viggo "Hell, it’s practically free food."

    voice "startnarratorline9.ogg"
    "*The tension between Isak and Tobias grows.*"

    voice "startnarratorline10.ogg"
    "*But Tobias doesn’t stop. He finishes scanning the fourth bun and heads toward the door.*"


    hide viggo

    show isak normal at left
    
    voice "startisakline10.ogg"
    isak "I’m not going to let you keep going like this."

    voice "startisakline11.ogg"
    isak "One day, you’re going to get caught."

    menu:
        "Tobias brushes off Isak and keeps walking out with the stolen pastries":
            $ tobias_stop = False
            jump bakery_confrontation
        "Tobias listens to Isak and decides to return the pastries":
            $ tobias_stop = True
            jump bakery_return


label bakery_confrontation:
    scene bakery_outside with fade
    show tobias normal at center

    voice "bakeryconfrontationnarratorline1.ogg"
    "*As Tobias walks out with his bag full of pastries, Isak steps in front of him, blocking the exit just slightly. His expression is serious.*"

    hide tobias
    show isak normal at left        

    voice "startisakline12.ogg"
    isak "Tobias, listen. I know you’re not trying to hurt anyone, but what you’re doing is wrong."

    voice "startisakline13.ogg"
    isak "You can’t keep pretending this is a harmless hack."

    voice "startisakline14.ogg"
    isak "You might think it’s clever now, but one day it’s going to come back and hit you harder than you expect."

    voice "startisakline15.ogg"
    isak "And when it does... it won’t be just about some buns. It’ll be about trust. About your name. Your future."


    hide isak
    show tobias normal at center

    voice "starttobiasline15.ogg"
    tobias "I don’t see it that way. I’m not hurting anyone."

    voice "starttopiasline16.ogg"
    tobias "What, you think they care about a couple of buns?"

    voice "starttobiasline17.ogg"
    tobias "I’m just taking what’s *mine*. I come here all the time. I’ve supported this place."

    voice "starttobiasline18.ogg"
    tobias "It’s not like I’m robbing the register."

    voice "starttobiasline19.ogg"
    tobias "I mean... where’s the harm, really?"


    hide tobias
    show viggo normal at right

    voice "startviggoline8.ogg"
    viggo "It’s not that big a deal. Let’s not make this into something it’s not."

    voice "startviggoline9.ogg"
    viggo "Seriously, Isak. It’s just food. It’s not like he’s breaking into someone’s house."

    voice "startviggoline10.ogg"
    viggo "You’re acting like this is grand theft or something."


    hide viggo
    show isak normal at left

    voice "startisakline16.ogg"
    isak "It *is* a big deal. Not because it’s about money or pastries. But because it’s about *who* you are."

    voice "startisakline17.ogg"
    isak "You’re making excuses. And every time you let yourself off the hook, it becomes easier to do it again."

    voice "startisakline18.ogg"
    isak "This is the kind of thinking that ruins people’s lives—not overnight, but slowly, one choice at a time."

    voice "startisakline19.ogg"
    isak "And I don’t want to stand by and watch you go down that road, man. I just can’t."


    menu:
        "Tobias argues with Isak and refuses to return the pastries":
            $ tobias_stop = False
            jump bakery_streak
        "Tobias decides to listen to Isak and return the pastries":
            $ tobias_stop = True
            jump bakery_return


label bakery_streak:
    scene bakery_outside with fade
    show tobias normal at center

    voice "startnarratorline11.ogg"
    "*Over the course of the next few days, Tobias visits the bakery again and again. Each time, he takes more pastries than before. *"

    voice "startnarratorline12.ogg"
    "*Isak’s concern turns to frustration, while Viggo is increasingly indifferent.*"


    voice "starttobiasline20.ogg"
    tobias "It’s like a game now. The more I take, the easier it gets. And I’m telling you, no one notices."

    voice "starttobiasline21.ogg"
    tobias "It’s honestly kind of thrilling. Like... I’m smarter than the whole system."


    hide tobias
    show viggo normal at right

    voice "startviggoline11.ogg"
    viggo "I mean, who’s really gonna care? They probably waste more buns than that every day."

    voice "startviggoline12.ogg"
    viggo "You’re not stealing from a grandma’s purse — it’s a faceless company."

    voice "startviggoline13.ogg"
    viggo "Honestly, it’s kind of a victimless crime."


    hide viggo
    show isak normal at left

    voice "startisakline20.ogg"
    isak "You both sound ridiculous."

    voice "startisakline21.ogg"
    isak "Just because someone isn’t watching you doesn’t mean it’s okay."

    voice "startisakline22.ogg"
    isak "You think it’s harmless now, but wait until it snowballs into something you *can’t* explain away."


    hide isak
    show tobias normal at center

    voice "starttobiasline22.ogg"
    tobias "Why do you keep acting like I’m some criminal mastermind?"

    voice "starttobiasline23.ogg"
    tobias "It’s just a few pastries, not a bank robbery."


    hide tobias
    show isak normal at left

    voice "startisakline23.ogg"
    isak "You’re *acting* like it’s harmless, but you know deep down it isn’t."

    voice "startisakline24.ogg"
    isak "Every time you walk out of here, I see you hesitate. That’s your conscience trying to speak up."

    voice "startisakline25.ogg"
    isak "If this really felt right, you wouldn’t need to justify it every time."


    hide isak
    show viggo normal at right

    voice "startviggoline14.ogg"
    viggo "Okay, okay, enough with the guilt trip."

    voice "startviggoline15.ogg"
    viggo "If Tobias wants to take advantage of a broken system, that’s on him."

    voice "startviggoline16.ogg"
    viggo "We’re not his babysitters."


    hide viggo
    show tobias normal at center

    voice "startnarratorline13.ogg"
    "*Tobias shifts uncomfortably, looking down at his bag. He doesn't say anything right away.*"

    voice "startnarratorline14.ogg"
    "*The laughter he used to share with Viggo feels more hollow now.*"

    voice "startnarratorline15.ogg"
    "*Isak's words echo in his mind as he steps toward the door.*"


    voice "starttobiasline24.ogg"
    tobias "Maybe you’re right... or maybe I’m already in too deep."

    voice "starttobiasline25.ogg"
    tobias "But it’s too easy to stop now."

    voice "startnarratorline16.ogg"
    "*He walks out once again, pastries hidden in his bag. But this time, his heart feels heavy, like the consequences of his actions are closing in.*"

    menu:
        "Tobias continues with his streak, despite his doubts":
            $ tobias_stop = False
            jump bakery_consequence
        "Tobias finally feels guilty and decides to stop stealing":
            $ tobias_stop = True
            jump bakery_return


label bakery_consequence:
    scene bakery_day with fade
    show tobias normal at center

    voice "startnarratorline17.ogg"
    "*Tobias walks into the bakery again, feeling the familiar thrill of getting away with his actions.*"

    voice "startnarratorline18.ogg"
    "*He glances around casually, like always. But something feels different today.*"
    
    voice "startnarratorline19.ogg"
    "*This time, there’s someone watching. A manager stands by the corner of the self-checkout area, arms crossed, eyes locked on Tobias.*"

    hide tobias
    show manager angry at center

    voice "startmanagerline1.ogg"
    manager "I see you've been here quite a bit lately. Always grabbing more than you're paying for."

    voice "startnarratorline20.ogg"
    "*His voice is sharp. Loud enough to turn a few heads.*"

    hide manager
    show tobias normal at left

    voice "startnarratorline21.ogg"
    "*Tobias freezes mid-scan, his hand trembling slightly.*"

    voice "startnarratorline22.ogg"
    "*His bag is once again stuffed with three extra pastries. His heart begins to pound in his chest.*"

    voice "starttobiasline25.ogg"
    tobias "I—uh, I don’t know what you mean. I’m just buying some buns. Like I always do."

    voice "startnarratorline23.ogg"
    "*He forces a chuckle, but it doesn’t land. The tension in the room is thick.*"

    hide tobias
    show manager angry at center

    voice "startmanagerline2.ogg"
    manager "Don't play dumb with me. I’ve been watching the cameras. You’ve been stealing."

    voice "startmanagerline3.ogg"
    manager "Every. Single. Time."

    voice "startnarratorlien24.ogg"
    "*The manager steps closer, voice lower now but even more serious.*"

    voice "startmanagerline4.ogg"
    manager "You’re not as clever as you think."

    show isak normal at left
    show viggo normal at right

    voice "startisakline26.ogg"
    isak "Tobias… this is it. You’re getting caught. This is what I was trying to warn you about."

    voice "startnarratorline25.ogg"
    "*Viggo looks uncomfortable now. He avoids eye contact, shoving his hands into his hoodie pocket.*"

    voice "startviggoline17.ogg"
    viggo "Damn, man… I didn’t think it’d actually come to this."

    hide isak
    hide viggo

    show manager angry at center

    voice "startnarratorline26.ogg"
    "*The manager grabs the bag from Tobias’ hand, pulling out the extra pastries one by one.*"

    voice "startnarratorline27.ogg"
    "*Each bun lands with a dull thud on the counter, like a gavel sealing a verdict.*"

    voice "startmanagerline5.ogg"
    manager "So what’s it gonna be?"

    voice "startmanagerline6.ogg"
    manager "You can pay for these right now… or I call the police."

    voice "startnarratorline28.ogg"
    "*Tobias stares at the pastries, then at the manager. He can feel the eyes of other customers. The shame, the heat rising in his face.*"

    voice "startnarratorline29.ogg"
    "*His mind races — excuses, escapes, anything. But the weight of his choices is undeniable now.*"

    menu:
        "Tobias apologizes and tries to make things right":
            $ tobias_stop = True
            jump bakery_return
        "Tobias tries to deny it and make a run for it":
            $ tobias_stop = False
            jump bakery_escape


label bakery_escape:
    scene bakery_outside with fade
    show tobias normal at center
    show manager angry at center

    voice "startnarratorline30.ogg"
    "*Tobias’s eyes dart toward the exit. Panic grips his chest as the manager steps closer.*"

    voice "startnarratorline31.ogg"
    "*In a split-second decision, he turns and bolts for the door, pastries still in his bag.*"

    voice "startmanagerline7.ogg"
    manager "Hey! HEY! Stop him!"

    voice "startnarratorline32.ogg"
    "*The sound of hurried footsteps echoes across the tile floor. Chairs scrape as startled customers move out of the way.*"

    voice "startnarratorline33.ogg"
    "*But the manager reacts quickly, cutting him off with surprising speed, standing firmly in his path.*"

    voice "startmanagerline8.ogg"
    manager "You’re not going anywhere, Tobias. This is over."

    voice "startnarratorline34.ogg"
    "*Tobias skids to a stop, breathing hard. His chest rises and falls like he’s run a marathon, though he’s barely taken five steps.*"

    hide manager angry
    show tobias normal at left

    voice "startnarratorline35.ogg"
    "*His voice trembles — not with fear, but something deeper. Regret, maybe.*"

    voice "starttobiasline28.ogg"
    tobias "I didn’t want this. I... I just wanted to feel like I had control."

    voice "starttobiasline27.ogg"
    tobias "Like... for once, I could make the rules."

    voice "startnarratorline36.ogg"
    "*He looks down at the bag, now crumpled from the scuffle. The pastries inside feel heavier than ever.*"

    voice "startnarratorline37.ogg"
    "*The manager pulls out his phone and dials security.*"

    show isak normal at left
    show viggo normal at right

    voice "startnarratorline38.ogg"
    "*Moments later, two security guards arrive. Calm but firm, they take Tobias by the arms.*"

    voice "startnarratorline39.ogg"
    "*The bakery falls into a hush as the guards escort him toward the exit.*"

    voice "startisakline28.ogg"
    isak "You should’ve stopped, Tobias."

    voice "startisakline29.ogg"
    isak "We could’ve helped you before it got to this."

    voice "startnarratorline40.ogg"
    "*Viggo watches silently, guilt flickering in his expression. For once, he has no clever comment.*"

    voice "startnarratorline41.ogg"
    "*Tobias doesn’t resist. He just walks, head low, as the scene fades.*"

    return


label bakery_return:
    scene bakery_day with fade
    show tobias normal at center

    voice "startnarratorline42.ogg"
    "*Tobias slowly walks back to the self-checkout counter, each step heavier than the last.*"

    voice "startnarratorline43.ogg"
    "*He opens his bag and pulls the pastries out one by one, placing them carefully on the counter.*"

    voice "startnarratorline44.ogg"
    "*The beeping of the scanner feels louder than usual, echoing his guilt as he pays for each item in silence.*"

    scene bakery_outside with fade

    voice "starttobisasline28.ogg"
    tobias "I... I didn’t realize how far I’d gone."

    voice "starttobiasline29.ogg"
    tobias "I kept telling myself it wasn’t a big deal. That no one would care."

    voice "starttobiasline30.ogg"
    tobias "But I knew. Deep down, I knew."

    voice "startnarratorline45.ogg"
    "*He pauses, staring at the screen as the total flashes.*"

    voice "starttobiasline31.ogg"
    tobias "It’s not worth it. None of this is worth it."

    show isak normal at left
    show viggo normal at right

    voice "startisakline30.ogg"
    isak "I’m proud of you, man. This is the right choice."

    voice "startisakline31.ogg"
    isak "It takes guts to admit when you’re wrong and actually do something about it."

    voice "startviggoline18.ogg"
    viggo "Yeah... I mean, it’s not easy to back down, especially after going all in like that."

    voice "startviggoline19.ogg"
    viggo "You did good, Tobias. Really."

    voice "startnarratorline46.ogg"
    "*Tobias looks at them, the tension in his shoulders starting to ease.*"

    voice "startnarratorline47.ogg"
    "*For once, there’s no grin, no cocky remark — just quiet honesty.*"

    hide isak
    hide viggo

    show tobias normal at center

    voice "startnarratorline48.ogg"
    "*He finishes paying, the receipt printing with a soft whirr. Tobias grabs it, staring down at it like it’s more than just numbers.*"

    voice "starttobiasline32.ogg"
    tobias "I guess I just... lost track of what mattered."

    voice "starttobiasline33.ogg"
    tobias "I got caught up in the rush. The idea of beating the system."

    voice "starttobiasline34.ogg"
    tobias "But all I was doing was fooling myself."

    voice "startnarratorline49.ogg"
    "*He tucks the receipt away and picks up the paid pastries. There’s no thrill this time — only relief.*"

    voice "startnarratorline50.ogg"
    "*As the three of them step outside together, the fresh air feels different. Cleaner. Lighter.*"

    voice "startnarratorline51.ogg"
    "*Tobias knows this won’t be the last time he’s tempted by the easy way out, but for now, he’s choosing something better.*"

    return
