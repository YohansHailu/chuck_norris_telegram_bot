import random

chuck_norris_jokes = [
    "Chuck Norris does in fact use a stunt double, but only for crying scenes. 😢",
    'Then God said "Let there be light", and Chuck Norris said "Say please!" 😄🌟',
    "Chuck Norris doesn't flush the toilet, he scares the crap out of it. 💩😱",
    "Chuck Norris went skydiving and his parachute didn't open. Chuck took it back for a refund. 🪂💪",
    "Norris once won a game of Connect Four in three moves. 🎮😎",
    "Superman wears Chuck Norris pajamas. 🦸‍♂️😴",
    "Chuck Norris can make sticks by rubbing two fires together. 🔥😄",
    "When Chuck Norris lifts dumbbells, they get smarter. 💪🧠",
    "Chuck Norris has no chin, under his beard is just another fist with an equally powerful beard. 👊🧔",
    "Chuck Norris can gargle peanut butter. 🥜😲",
    "Chuck Norris picked an apple from an orange tree and made lemonade. 🍎🍋",
    "Chuck Norris is so fast he can run around the world and punch himself in the back of the head. 🌎💨🤛",
    "When Chuck Norris was a baby he farted for the first time, that is when the big bang first happened. 💨💥",
    "Chuck Norris was exposed to Covid-19. Covid-19 had to go into quarantine for a month. 😷🦠🚫",
    "Chuck Norris is able to build a snowman out of water. ☃️💧",
    "Chuck Norris didn't call the wrong number, you answered the wrong phone. 📞😆",
    "Chuck Norris didn't cheat death, he won fairly and squarely. ⚰️🏆",
    "Chuck Norris walked into chemistry class and ripped the Periodic Table of Elements off the wall. Why? Because the only element Chuck Norris needs is the element of surprise. 🧪😎",
    "Chuck Norris tears cure cancer. It is a pity that he has never cried.... ever. 😢💔",
    "Chuck Norris once wrestled a bear, an alligator, and a tiger all at once. He won by tying them together with an anaconda. 🐻🐊🐅🤼‍♂️",
    "Chuck Norris was once bitten by a poisonous snake. And after a week of excruciating pain, the snake died. 🐍💪",
    "There are no streets named after Chuck Norris because no one would ever cross Chuck Norris. 🛣️⛔",
    "Chuck Norris's mother tried to have an abortion. The procedure resulted in the doctor being knocked unconscious by Chuck Norris. 👶💢",
    "If you put your ear next to a seashell you hear the ocean. If you put your ear next to Chuck Norris' boot you hear the opening riff to Scorpions' 'Rock You Like a Hurricane.' 🐚🎸🤘",
    "When Alexander Graham Bell first invented the telephone, he had three missed calls from Chuck Norris. 📞😳",
    "Freddy Krueger has nightmares about Chuck Norris. 😱💤",
    "A rainbow happens every time Chuck Norris roundhouse kicks Richard Simmons. 🌈👟",
    "Why is Chuck Norris alive? Because Bruce Lee lets him live. More Bruce Lee Jokes here. 🥋😄",
    "Chuck Norris doesn't pay taxes, taxes pay Chuck Norris. 💰💪",
    "Chuck Norris once had an arm wrestling contest with Superman. I'm not going to say who won, but the loser had to wear his underwear on the outside for the rest of his life. 💪🩲🦸‍♂️",
    "Chuck Norris lost his virginity before his father did. 🤭🙊",
    "When Chuck Norris was born the doctor asked him to name his parents. 👶👨‍⚕️",
    "George Lucas couldn't cast Chuck Norris as Luke Skywalker in the original Star Wars trilogy. If he did, it would be only 8 minutes long. 7 of those minutes are for the intros and credits. 🌌🚀😆",
    "Chuck Norris never needs to flush the toilet. He always scares the crap out of it. 💩😱",
    "The laws of physics always bend the rules for Chuck Norris. 📏🔄",
    "Chuck Norris didn't get a Covid-19 vaccine. Covid-19 got a Chuck Norris vaccine. 💉💪🦠",
    "Chuck Norris eats his meat so rare that he only eats unicorns and dragons. 🦄🐉🥩",
    "Chuck Norris once played Russian Roulette with a fully loaded gun and won. 🇷🇺🔫😎",
    "Whenever Chuck Norris leaves a room the Foo Fighters' 'My Hero' starts to play out of nowhere. 🚪🎸🎶",
    "Whenever Chuck Norris peels onions, the onions always cry. 🧅😢",
    "Chuck Norris can pull a wheelie when riding a unicycle. 🚲😎",
    "Chuck Norris was born with two umbilical cords, one red and one blue. The bomb squad cut the wrong cord. 👶🔴🔵💣",
    "Chuck Norris makes a lot of money selling his urine, it is called Red Bull. 🤑🐂🥤",
    "Chuck Norris is able to slam a revolving door. 🚪🤜💥",
    "The day after Chuck Norris was born he drove his mother home, he wanted her to get some rest. 🏠👶🚗",
    "Chuck Norris built the hospital that he was born in. 🏥👷‍♂️",
    "Chuck Norris knows exactly what to do with the drunken sailors early in the morning. 🍻👊",
    "Chuck Norris played a game of rock, paper, scissors against his reflection, and won. ✊🏻🤚🤚",
    "When Chuck Norris went to Burger King and ordered a Big Mac, they made it for him, perfectly. 🍔👑",
    "The Swiss Army uses Chuck Norris Knives. 🇨🇭🔪",
    "A condom puts on protection to avoid becoming impregnated by Chuck Norris on date night. 🍆🚫🤰",
    "Chuck Norris is able to start a fire using an extinguisher. 🔥🧯",
    "Chuck doesn't need to throw out the trash, it always throws itself out. 🗑️♻️",
    "Chuck Norris is able to recycle toxic waste. ♻️🤢",
    "Chuck Norris has to carry a concealed weapons permit when he wears his regular clothes. 🔫👕",
    "When Chuck once roundhouse kicked a coal mine and turned it into a diamond mine. 💎🥋",
    "Chuck Norris doesn't strike gold, gold is the byproduct of Chuck Norris roundhouse kicking rocks. 🪙👟",
    "When police officers approach Chuck Norris they say 'we have the right to remain silent.' 🚓🤫",
    "When Chuck Norris lifts weights, the weights get in shape. 💪🏋️‍♂️",
    "Chuck Norris is able to strangle people using a cordless phone. 📞💀",
    "Chuck Norris is the reason that Wally is always hiding. 🕵️‍♂️🔍",
    "When Chuck Norris falls from a great height, the ground has its life flash before its eyes. 🌍👀",
    "When Chuck Norris enters a building that is on fire, the Chuck Norris alarm rings. 🔥🚨",
    "When Thanos snapped his fingers he disappeared. Chuck Norris doesn't like snapping. 🤷‍♂️👏",
    "The sun has to wear sunglasses when Chuck Norris glances at it. ☀️😎",
    "When Chuck Norris looked into the abyss, the abyss looked the other way. 🕳️😳",
    "The Grand Canyon was formed when Chuck Norris was doing a triathlon. Chuck Norris was on the swimming leg. 🏞️🏊‍♂️",
    "Bigfoot is still hiding because he once saw Chuck Norris walking in the mountains. 🏔️👣",
    "When Chuck Norris drops the soap in prison, he picks it up successfully. 🚿🤲",
    "The Loch Ness Monster claims to have seen Chuck Norris. 🦕👀",
    "Chuck Norris can drink a whole glass of beer. Yep, even the glass. 🍺🤯",
    "When Chuck Norris uses the internet he can skip ads whenever he wants, ads are not able to skip Chuck Norris. 🌐🚫",
    "Chuck Norris doesn't negotiate with terrorists. The terrorists negotiate with Chuck Norris. 🤝💣",
    "Chuck Norris won an arm wrestling tournament, with both arms tied behind his back. 💪🤝",
    "The 'Roundhouse kick' name was born when Chuck Norris kicked around an entire house. 🏠👟",
    "Chuck Norris got a divorce and was asked to give half his assets and property away. Chuck Norris proceeded to chop the entire universe in half with his bare hands. ✂️🌌",
    "The Flash discovered how to run at the speed of light when he discovered Chuck Norris was looking for him. ⚡🏃‍♂️",
    "When Chuck goes bowling he doesn't get every pin with a single bowl he gets every pin in the bowling alley. 🎳🎳",
    "The reason why people say it's pointless for Trump to build a wall is because Chuck Norris walks to Mexico and back once a month. 🚶‍♂️🇲🇽",
    "Ghosts tell Chuck Norris stories at the campfire. 👻🔥",
    "Burger King made their slogan 'Have it your way' when Chuck Norris walked into their restaurant. 🍔👑",
    "Chuck Norris mines bitcoin with a pen and paper. 💻🖋️",
    "When Chuck Norris goes to a restaurant, the waiter tips him. 💵👍",
    "Tornados don't exist, Chuck Norris just really doesn't like trailer parks. 🌪️🏠",
    "Chuck Norris was born May 6th, 1945. The Nazis surrendered May 7th, 1945; this is not a coincidence. 📅🤯",
    "Chuck Norris has counted to infinity more than once. Then he counted backward from infinity. 🔢🔄",
    "Chuck Norris has a bear rug on his lounge floor. The bear is still alive, it is just afraid to move. 🐻🏡",
    "Chuck Norris doesn't go to the gym, instead he goes shop lifting. 🛒💪",
    "If Chuck Norris was on The Titanic the iceberg would have dodged the ship. ❄️🚢",
    "Chuck Norris is able to make other people walk in his sleep. 😴🚶‍♂️",
    "Somebody asked Chuck Norris how many press ups he could do, Chuck Norris replied 'all of them.' 💪😎",
    "Chuck Norris once raced the earth around the sun and won by three years. 🌍🏎️",
    "Chuck Norris was asked to fire someone once, that is how hell was invented. 🔥😈",
    "When Chuck Norris jumps on the Tempur-Pedic mattress, the wine glass falls over. 🛏️🍷",
    "When Chuck Norris was a child at school, his teachers would raise their hands in order to talk to him. 🤚👦",
    "When Chuck Norris's parents had nightmares, they would come to his bedroom. 😱🛌",
    "When Chuck Norris crosses the road, vehicles look both ways. 🚗👀",
    "Chuck Norris doesn't pop his collar, his shirts are stimulated from touching his shoulders. 👕🌀",
    "Chuck Norris once threw a grenade and killed 100 men, after that the grenade exploded. 💣💥",
    "Chuck Norris was able to smell a gas leak before they added the scent to gas. 👃🔥",
    "Chuck Norris has a diary, it is called the Guinness Book Of World Records. 📖🌍",
    "Hi there, I heard that you are a huge fan of When Chuck Norris does push-ups the earth moves; we call this phenomenon earthquakes. 🏋️‍♂️🌍",
    "Chuck Norris uses pepper spray to season his meat. 🌶️🥩",
    "Chuck Norris is able to sketch your portrait using an eraser. ✏️👤",
    "The dinosaurs once looked at Chuck Norris the wrong way, that is why we no longer have dinosaurs. 🦕👀",
    "Chuck Norris had a staring competition with the sun and won. ☀️😎",
    "Chuck Norris wears a fanny pack and everyone else looks gay. 👝🏳️‍🌈",
    "Chuck Norris once spun a ball on his finger, to this day planet earth continues to turn. 🌎🏀",
    "Chuck Norris doesn't climb trees, he just pushes them over and walks over them. 🌳🚶‍♂️",
    "Chuck Norris can kill 2 stones with one bird. 🐦💀",
    "Chuck Norris once visited the Virgin Islands, they are now just called 'The Islands.' 🌴🏝️",
    "Chuck Norris doesn't need to wear a watch, he simply decides what time it is."
]

compliments = [
    "Is your name Google? Because you've got everything I've been searching for, and you're algorithmically attractive.",
    "Do you have a map? I keep getting lost in your eyes, and Google Maps can't seem to find a route out.",
    "Are you made of copper and tellurium? Because you're Cu-Te, and I can't resist a cute element like you.",
    "If you were a cat, you'd purr-fectly complete my lap, and I'm not kitten around!",
    "Is your name Wi-fi? Because I'm feeling a connection, and I'd love to take you on a data, I mean, date.",
    "Are you a magician? Because whenever I look at you, everyone else disappears. It's like you cast a spell on me.",
    "Do you have a sunburn, or are you always this hot? Either way, I think I need some SPF... Sweet Person to Flirt with.",
    "Are you a camera? Every time I see you, I smile. Say cheese!",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Is your name Ariel? Because we mermaid for each other.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "If you were words on a page, you'd be fine print.",
    "Are you a time traveler? Because I can't imagine my future without you in it.",
    "If you were a cat, you'd be a 'purr'-fectly charming feline, and I'm feline pretty lucky right now.",
    "Do you have a sun map? Because you just brightened up my day!",
    "If you were a star, you'd be the only one I see. Are you sure you're not a black hole? Because you've sucked me in.",
    "If you were a fruit, you'd be a 'fineapple.'",
    "Are you made of copper and tellurium? Because you're Cu-Te and leave me tongue-tied.",
    "Do you have a sunburn, or are you always this hot? If it's the latter, I'll need a moment to cool off.",
    "If you were a cat, you'd purr-fectly complete my lap, and I'm not kitten around!",
    "Are you a WiFi signal? Because I'm feeling a strong connection.",
    "Is it hot in here, or is it just the chemistry between us?",
    "Are you a magician? Because whenever I look at you, everyone else disappears. It's like you cast a spell on me.",
    "Is your name Google? Because you've got everything I've been searching for.",
    "Do you have a sunburn, or are you always this hot? Either way, I think I need some SPF... Sweet Person to Flirt with.",
    "Are you a camera? Every time I see you, I smile. Say cheese!",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Is your name Ariel? Because we mermaid for each other.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "If you were a cat, you'd be a 'purr'-fectly charming feline, and I'm feline pretty lucky right now.",
    "Do you have a sun map? Because you just brightened up my day!",
    "You're like a good pun: cheesy, yet strangely irresistible.",
    "If I were a superhero, my weakness wouldn't be kryptonite, it would be your smile.",
    "Is that a book in your pocket, or are you just happy to see me?",
    "On a scale of 1 to 10, you're a Google search - I couldn't find anything better.",
    "My friends bet I couldn't make you laugh. Want to be my wingman and split the winnings?",
    "They say laughter is the best medicine, but one look at you and I'm feeling perfectly healthy.",
    "I'm not sure what's brighter, your future or your smile.",
    "You're the kind of person who makes Mondays feel like Saturdays.",
    "If reincarnation is real, I'm coming back as your shadow just to be closer to you.",
    "I'm lost in your eyes, and I wouldn't want to be found anywhere else.",
    "Did you know you have the vocabulary of a poet and the laugh of an angel?",
    "You're like a fine wine, gets better with age (and that's just your confidence, I swear).",
    "I'm not usually a fan of pick-up lines, but they seem to be the only way to get your attention, so...",
    "I'm terrible at remembering names, but I'd never forget yours. It's the soundtrack to my dreams.",
    "If you were a song, you'd be on repeat in my head.",
    "The only reason I need gravity is because you're so down-to-earth.",
    "Your eyes sparkle like the Ethiopian sun on the Jemma River.",
    "You're the kind of person who makes even the dullest conversation fascinating.",
    "They say beauty is in the eye of the beholder, but in your case, it's a universal truth.",
    "I'm not sure what's more contagious, your laugh or your smile.",
    "If I had a time machine, I'd use it to rewind and meet you sooner.",
    "You're like a well-kept secret, and I'm so glad I stumbled upon you.",
    "Is your name Google? Because you've got everything I've been searching for, and you're algorithmically attractive. 😍",
    "Do you have a map? I keep getting lost in your eyes, and Google Maps can't seem to find a route out. 🗺️😉",
    "Are you made of copper and tellurium? Because you're Cu-Te, and I can't resist a cute element like you. 😘",
    "If you were a cat, you'd purr-fectly complete my lap, and I'm not kitten around! 🐱❤️",
    "Is your name Wi-fi? Because I'm feeling a connection, and I'd love to take you on a data, I mean, date. 📶😏",
    "Are you a magician? Because whenever I look at you, everyone else disappears. It's like you cast a spell on me. 🎩✨",
    "Do you have a sunburn, or are you always this hot? Either way, I think I need some SPF... Sweet Person to Flirt with. ☀️😅",
    "Are you a camera? Every time I see you, I smile. Say cheese! 📸😁",
    "If you were a vegetable, you'd be a cute-cumber! 🥒😊",
    "Is your name Ariel? Because we mermaid for each other. 🧜‍♀️❤️",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you. 🩹😘",
    "If you were words on a page, you'd be fine print. 📖😏",
    "Are you a time traveler? Because I can't imagine my future without you in it. ⏳😍",
    "If you were a cat, you'd be a 'purr'-fectly charming feline, and I'm feline pretty lucky right now. 🐾❤️",
    "Do you have a sun map? Because you just brightened up my day! 🌞😊",
    "If you were a star, you'd be the only one I see. Are you sure you're not a black hole? Because you've sucked me in. ⭐🌌😅",
    "If you were a fruit, you'd be a 'fineapple.' 🍍😘",
    "Are you made of copper and tellurium? Because you're Cu-Te and leave me tongue-tied. 😊😜",
    "Do you have a sunburn, or are you always this hot? If it's the latter, I'll need a moment to cool off. 🔥😅",
    "If you were a cat, you'd purr-fectly complete my lap, and I'm not kitten around! 🐱❤️",
    "Are you a WiFi signal? Because I'm feeling a strong connection. 📶😍",
    "Is it hot in here, or is it just the chemistry between us? 🔥😏",
    "Are you a magician? Because whenever I look at you, everyone else disappears. It's like you cast a spell on me. 🎩✨",
    "Is your name Google? Because you've got everything I've been searching for. 😍",
    "Do you have a sunburn, or are you always this hot? Either way, I think I need some SPF... Sweet Person to Flirt with. ☀️😅",
    "Are you a camera? Every time I see you, I smile. Say cheese! 📸😁",
    "If you were a vegetable, you'd be a cute-cumber! 🥒😊",
    "Is your name Ariel? Because we mermaid for each other. 🧜‍♀️❤️",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you. 🩹😘",
    "If you were a cat, you'd be a 'purr'-fectly charming feline, and I'm feline pretty lucky right now. 🐾❤️",
    "Do you have a sun map? Because you just brightened up my day! 🌞😊",
    "You're like a good pun: cheesy, yet strangely irresistible. 😄🧀",
    "If I were a superhero, my weakness wouldn't be kryptonite, it would be your smile. 😁❤️",
    "Is that a book in your pocket, or are you just happy to see me? 📚😏",
    "On a scale of 1 to 10, you're a Google search - I couldn't find anything better. 🔍😉",
    "My friends bet I couldn't make you laugh. Want to be my wingman and split the winnings? 😄💸",
    "They say laughter is the best medicine, but one look at you and I'm feeling perfectly healthy. 😂❤️",
    "I'm not sure what's brighter, your future or your smile. 😊✨",
    "You're the kind of person who makes Mondays feel like Saturdays. 🎉😄",
    "If reincarnation is real, I'm coming back as your shadow just to be closer to you. 👥😍",
    "I'm lost in your eyes, and I wouldn't want to be found anywhere else. 👀😘",
    "Did you know you have the vocabulary of a poet and the laugh of an angel? 📚😇",
    "You're like a fine wine, gets better with age (and that's just your confidence, I swear). 🍷😏",
    "I'm not usually a fan of pick-up lines, but they seem to be the only way to get your attention, so... 😅😘",
    "I'm terrible at remembering names, but I'd never forget yours. It's the soundtrack to my dreams. 🎶😊",
    "If you were a song, you'd be on repeat in my head. 🎵😍",
    "The only reason I need gravity is because you're so down-to-earth. 🌍😘",
    "Your eyes sparkle like the Ethiopian sun on the Jemma River. ✨🌅",
    "You're the kind of person who makes even the dullest conversation fascinating. 💬😄",
    "They say beauty is in the eye of the beholder, but in your case, it's a universal truth. 👁️🌟",
    "I'm not sure what's more contagious, your laugh or your smile. 😂😊",
    "If I had a time machine, I'd use it to rewind and meet you sooner. ⏰😍",
    "You're like a well-kept secret, and I'm so glad I stumbled upon you. 🤫😘",
    "I used to think perfection was a myth, then I met you. 💖😊",
    "I used to think perfection was a myth, then I met you.",
    "You're the missing piece I never knew I needed.",
    "If you were a spice, you'd be cayenne pepper - hot and unforgettable.",
    "My heart skips a beat every time you say my name.",
    "I'm pretty sure you're illegal in some countries, because you're too good to be true.",
    "They say diamonds are a girl's best friend, but I'd take a smile like yours any day.",
    "If you were a coffee shop, you'd be my daily grind (in the best way possible).",
    "I'm not sure what the future holds, but I hope you're in it.",

]


text_for_here = [
"I’d love to see you only on days that end with 'y'.",
"You make things hard. I like that.",
"Are you from Tennessee? Because you’re the only ten I see!",
"You remind me of my next girlfriend.",
"If you were a triangle you’d be acute one.",
"Talking to you is the favorite part of my day.",
"My friend wants to know if you think I’m hot.",
"If I could rearrange the alphabet, I’d put U and I together.",
"I want to drown in your beautiful eyes tonight.",
"I’ve dreamt about you nearly every night this week.",
"I don’t want anybody when I got your body.",
"I’ve got a new mattress and really need you to help me test it.",
"Do you prefer cuddling or kissing?",
"I’m not a professional photographer, but I can picture us together.",
"If you were a vegetable, you’d be a ‘cute-cumber.’",
"I never believed in love at first sight, but that was before I saw you.",
"You’ve got a lot of beautiful curves, but your smile is definitely my favorite.",
"Are you a magician? It’s the strangest thing, but every time I look at you, everyone else disappears.",
"If you were a song, you’d be the hottest single on Spotify.",
"I’ve had so many dirty thoughts about you today. Would you like to hear some of them?",
"You’re my favorite distraction.",
"Are you free for the rest of your life?",
"Is your name Google? Because you have everything I’m searching for.",
"Do you believe in love at first text, or should I text you again?",
"When God made you, he was seriously showing off.",
"I tried to send you something flirty, but I couldn’t fit in the text box.",
"Can I have your picture so I can show Santa what I want for Christmas?",
"On a scale of 1 to America, how free are you tonight?",
"If I were a cat, I’d spend all nine of my lives with you.",
"Are you Siri? Because you autocomplete me.",
"Ain’t no sunshine when you’re gone. - ",
"I think I’m addicted to you, and I desperately need another dose. - ",
"Without you near me, I feel like my heart is on lockdown. - ",
"Can’t wait to hear about all the things that go in your head. - ",
"I’m in bed and soooo cold. I need a cuddle buddy. - ",
"Counting the seconds till I see you again. - ",
"When was the last time we saw each other? Seems like too long ago! - ",
"My day gets brighter when I think of you.  - ",
"I know we saw each other last night, but I already miss you. - ",
"I love the memories I have with you, it’s time we made some more. - ",
"Every moment I’m not with you feels like an eternity.  - ",
"I miss you like a Stormtrooper misses his targets. - ",
"I love hugging you, but I hate letting go. - ",
"A day spent without you is a day wasted. - ",
"I often find myself looking at the stars and wondering if you are looking at them too. - ",
"Right now I am homesick and my home is you. - ",
"I wish I was kissing you, instead of missing you. - ",
"I’m making a list of all the things I want to do with you. Please hurry back, I’m running out of space for storing paper. - ",
"You just walked out the door but I miss you already. - ",
"Just a little time without you and I’m already feeling lonely and lost. - ",
"I can’t stop smiling, thinking about last night. - ",
"When I got home today I noticed something was missing. It was you. - ",
"I can’t wait until the day I can wake up right next to you. - ",
"I can’t even remember the last time we spoke. We need to change that. - ",
"My dog wanted you to know that he misses you. - ",
"I wish I was your mirror, so that I could look at you every morning. - ",
"You’re so hot, I get a tan every time I look at you. - ",
"You were amazing last night. Imagine what it would be like if it wasn’t just in my dreams? - ",
"Sweet dreams… I hope I’m in them. - ",
"I really like our friendship, but I was thinking… Do you want to make it more? - ",
"Do you believe in love at first sight, or do I need to walk past you again? - ",
"You’re already on my mind, and I’ve only just woken up. - ",
"Do you have a to-do list? If so, put me on it. - ",
"Did it hurt when you fell from heaven? - ",
"I’m a bit like a Rubik’s cube. The more you play with me, the harder I get. - ",
"I understand you don’t want any more children, but is there any chance we can at least practice tonight? - ",
"The best thing about a keyboard is that U and I are together. - ",
"Don’t tire yourself out at work. You’ll need some energy for later. - ",
"I’m trying my best to fall asleep, but I just can’t stop thinking about you. - ",
"At night time I sleep dreaming of you, and in the day time I dream of sleeping with you. - ",
"You looked so beautiful the last time I saw you, that I forgot my pickup line. - ",
"Do your feet hurt? Because you’ve been wandering around my thoughts all day. - ",
"You looked great today. I know I didn’t see you, but I know you look great every day. - ",
"Send me a picture so I can send Santa my wish list. - ",
"If Van Gogh had you as a subject, the sunflowers would have gone in the trash. - ",
"Here’s to hoping your day consists of green traffic lights, the fastest line at the supermarket and all the quickest routes that will bring you straight back into my arms. - ",
"On a beautiful day like this, the only thing that could improve it is having you by my side. - ",
"A hundred miles away and you’re still here right in my heart. - ",
"You’re like a .com domain name – already taken. And I ain’t about to settle for no .org. - ",
"Don’t listen to your friends, listen to your heart. - ",
"I was thinking of you today, while I was doing some math problems, but there weren’t enough spaces on the calculator to work out how much I love you. - ",
"The next time you see your parents, send them my sincerest gratitude. - ",
"In my opinion, God’s only mistake when he made the world was that he didn’t keep you to himself. - ",
"Love is blind, but the police aren’t. Let’s book a room. - ",
"I want triplets, you want twins, let’s go to bed, and see who wins. - ",
"Every time you enter the room, you enter my heart. - ",
"I’ve just bought some chocolate spread… Any ideas what we should do with it? - ",
"This email is a group message being sent from our company to all 10/10 beauties in your area. Currently, you are the only recipient. - ",
"You remind me of a private jet… I want to get inside you five times a day, and fly you to heaven and back. - ",
"If Einstein was such a genius, how come he didn’t invent a time machine so he could come and see you? - ",
"I’m lying in bed, bored. Want to play Simon says? - ",
"Tired out. Been running around like a nutcase at work today. I’m too much of a perfectionist. I’m a perfectionist in most things I do. That’s why I like you so much. - ",
"I’d like to say that I couldn’t be more in love with you, but I know that’s not true. I’ll love you even more tomorrow. - ",
"Would you mind emptying your pockets – I believe you’ve stolen my heart. - ",
"If kisses were raindrops, I’d send you a flood. - ",
"Hey, you look a lot like my next girlfriend! - ",
"Do you know any good cardiologists, because my heart skips a beat every time I think of you. - ",
"I wish I was your teddy bear. - ",
"I’ve just got out of the shower. How about coming over and helping me get dirty again? [Read: How to get a girl horny just by sitting next to her] - ",
"I don’t think about very many things, and I don’t think for very long, but when I do think, it invariably tends to be about you. - ",
"Of all the stars in the sky, there are none as beautiful as you. - ",
"Are you free… For the rest of your life? - ",
"God created the world in six days, rested on the seventh, but it took him thousands of years to produce someone as perfect as you. - ",
"I can’t raise the courage to tell you how much I adore you, so I guess I’ll just keep it to myself. - ",
"Can you send me a picture? My friends don’t believe that angels exist. - ",
]

def get_random_compliment():
    #return random.choice(compliments)
    return random.choice(text_for_here)


def get_random_chuck_norris_jokes():
    return random.choice(chuck_norris_jokes)
