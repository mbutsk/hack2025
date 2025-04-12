langs = ["ru", "en"]

# Переводы реплик персонажей
replicas = {
    "ru": {
        "hi":             "Привет! Здесь не будет длинных придесловий. Идея игры в том, что вы не знаете, что происходит в самом начале игры. Перед прохождением, прочитайте `README.md`. Язык можно сменить командой /change",
        "pigeon":         "*Вам пришло неизвестное письмо от голубя...*",
        "johnes1":        "Здравствуйте, агент Скотт. На данный момент проходит обновление ПО Ваших часов, а задание срочное. Письма в этой эпохе доставляются только таким путем, так что… надеюсь, оно дошло в целости. Вы должны нейтрализовать группировку бандитов под названием Evil Joe's. Это самая опасная группировка Далласа в этой ветке. Им поставляют оружие из 2427. Преступную сеть будем начинать уничтожать с этого момента. Ваша задача - победить как минимум 5 бандитов. Расположение - салун Томаса. Когда справитесь, отправляйте сигнал в штаб 1845 и ждите дальнейших указаний. Удачи!\n\n\nОт агента Джонса",
        "waiter":         "Здравствуйте, возьмете что-нибудь?",
        "saloon_you":     "Кто здесь... _читаете с бумажки_ Evil Joe's?",
        "saloon_bandits": "_Толпа бандитов подходят к тебе_",
        "manual1":        "_В этой мини игре вам нужно нажать на кнопку за ограниченное время. Чтобы начать мини игру, нажмите на кнопку снизу. После удачного попадения а одного бандита, следующий придет через некоторое время_",
        "shoot":          "Цель стала прямо возле вас",
        "inline":         "Вы нажали инлайн кнопку",
        "you_shoot":      "__Фух. Пора идти дальше__",
        "enter_year":     "Введите год...",
        "new_button":     "Скоро появится новая кнопка, жди ее",
        "hq_far_away":    "Штат слишком далеко",
        "hq_not_found":   "Штаб не найден",
        "johnes2":        "В 2427  ужас. Разработчики из этой организации, которая по данным разведки называется YEN.NEFER создали ИИ под кодовым названием NASTASYA. Он должен был помогать с грузоперевозками оружия по времени. Ему дали всю информацию о сети YEN.NEFER и дали несколько дней на изучение. Искусственный интеллект узнал слишком многое и решил, что ВСЕ люди такие, как эти бандиты и недостойны тому, чтобы он помогал им. YEN.NEFER дали ему слишком большой контроль на тот момент. NASTASYA творит ужас в 2427. Ты должен отправится туда. Ты появишься в случайном месте, найди путь",
        "robot1":         "_Вас встречает очень странный робот, который танцует тектоник без музыки_",
        "robot2":         "_Немного вглядываясь, Вы замечаете то, что у робота торчат провода в разных местах. Еще немного присмотревшись, вы видите то, что он полон дырок, но они заросли плесенью с красноватым оттенком_",
        "you_mind":       "_Куда я попал?.. Что с ним?_",
        "guard1":         "_В дали вы увидели охранную будку и выход._",
        "guard2":         "Эй, человечишка!",
        "guard3":         "Кто вы? И что здесь произошло?",
        "guard4":         "Хе-Хе, а я тебя не выпущу!",
        "guard5":         "_Вы увидели, что на стойке будки стоял маленький говорящий хомяк_",
        "guard6":         "Хочешь выйти, отгадай загадку!",
        "manual2":        "_Deepseek будет придумывать загадки и ответы на них. Могут потребоваться ресурсы компьютера. Продолжайте, только в том случае, если вы установили `deepseek-r1:7b` по гайду из README.md и у вас мощный компьютер. Загадки и ответы на них будут на английском языке_",
        "manual3":        "Компьютер может взорваться, так что здесь только один раунд + этот бро ошибаться может",
        "guard7":         "Не правильно! Ладно, пущу тебя, будешь должен. А правильный ответ был `{}`",
        "guard8":         "Во молодец, во дает! Ай-да {}",
        "notification":   "Вам пришло уведомление",
        "coord":          "Добрый день, агент Скотт. Ваши координаты - {}-{}",
        "robot_met":      "По пути вас встречает робот",
        "artist1":        "Я робот художник. Я должен нарисовать картину. Картину.",
        "artist2":        "Привет! Вчера я должен был нарисовать 2 портрета разных людей, но случайно нарисовал один с двумя слившимися людьми! Помоги вспомнить, кто на картине",
        "manual4":        "_Исскусственный интеллект слил изображения двух людей в одно. Выбери категорию и напиши 2 фамилии через знак `+`. Если у *персонажа* нет фамилии (вы поймете этот случай, если вам попадется он), пишите имя_",
        "manual5":        "_Ты должен написать фамилии двух людей через `+`_",
        "wrong_art":      "Не очень похоже... Может еще раз? Если ты не знаешь, посмотри на другой портрет",
        "artist3":        "Да! Это они. Спасибо, большое!",
        "stableman1":     "Привет! Я вытренировал 4 коней для скачек. Как думаешь, на кого поставить?",
        "stableman2":     "Ну вот и что за бред ты мне посоветовал?! Теперь я от тебя точно не отстану! Пока я не выиграю, ты отсюда не уйдешь",
        "stableman3":     "Ну вот! Люблю людей, с помощью которых я зарабатываю!",
        "nefer_guards":   "_На вас напали 3 охранника. Вы знаете что делать_",
        "nefer1":         "Зачем ты пришел сюда? Один из тех, кто пытается устранить меня? Давай сыграем в пару игр.",
        "nefer2":         "Ха! Ты не понял. У тебя просто *НЕТ* ВЫБОРА",
        "nefer3":         "Какой послушный, люблю таких!",
        "nefer4":         "Итак, начнем! Мы будем играть в...",
        "nefer5":         "Крестики-нолики!!!",
        "nefer6":         "Ты думаешь меня обмануть? Ха!",
        "nefer7":         "Давай продолжим делать вид, будто мы НЕ играли в поддавки)",
        "nefer8":         "А ты не так плох! Хороший мальчик. Так бы и почесала за ушком",
        "nefer9":         "Кто не успел, тот опоздал!",
        "nefer10":        "А я как всегда самая лучшая!",
        "nefer11":        "Итак, продолжаем! Я не понимаю смысл этой игры, но знаю, что *ВЫ* люди любите эту игру. Начинай!",
        "nefer12":        "Как жаль, что у меня нет рук!",
        "nefer13":        "А теперь самая интересная часть игры!",
        "nefer14":        "Пока ты играл, я собирала данные о тебе! По каждой твоей эмоции! Интересно, да? Я знаю, где ты работаешь, где ты жил, и чем ты занимался *КАЖДУЮ СЕКУНДУ*. Я не оставляю при жизни людей, которые пытались меня уничтожить",
        "nefer15":        "Просто убить тебя было бы *СЛИШКОМ* скучно, да и зачем? За тобой пришли бы твои дружки из компашки. Ты просто *не родишься*. Вот так я придумала! У тебя есть минута, пока твое время не закончилось! Звучит странно, но весело! Прощай",
        "nefer16":        "_Механическая рука выносит вас далеко на улицу_",
        "nefer17":        "_Вас положили возле того самого робота. Вы о чем-то догадываетесь, но уже слишком поздно..._",
        "end":            "Поздравляю с прохождением игры! Вы потратили {}. Вам доступно общение с Исскусственным интеллектом помощником и NASTASYA. Выберите с кем хотите общаться (только если вы установили нужную модель ollama). Желательно писать ему на английском",
        "changed":        "*Системный промпт изменен. Вы можете общаться с ИИ*",
        "choosepr":       "Выберите промпт"
    },

    "en": {
        "hi":             "Hi! There will be no long introductions. The idea of this game is that you don't know what is going on at the start of the game. Before playing, please read README.md. You can change language by /change command",
        "pigeon":         "You have received unknow letter from pigeon...",
        "johnes1":        "Hello, Agent Scott. Your watch is currently undergoing a software update, and the mission is urgent. Letters in this era are only delivered this way, so... I hope it arrived in one piece. You must neutralise a group of bandits called Evil Joe's. They're the most dangerous gang in Dallas in this branch. They're being supplied with weapons from 2427. We'll start destroying the criminal network from here on out. Your task is to defeat at least 5 gangsters. The location is Thomas' saloon. When you're done, send a signal to 1845 headquarters and wait for further instructions. Good luck!\n\n\nFrom Johnes",
        "waiter":         "Hello, will you take something?",
        "saloon_you":     "Who are... _you read from sheet of paper_ Evil Joe's?",
        "saloon_bandits": "*A bunch of bandits come up to you*",
        "manual1":        "_You have to press the button in 0.5s. To start the mini game, click on the button below. After a successful hit on one bandit, the next one will come after a while._",
        "shoot":          "There's a goal standing right next to you",
        "inline":         "You have pressed inline button",
        "you_shoot":      "Whew, it's time to move on",
        "enter_year":     "Enter the year...",
        "new_button":     "There will be a new button soon, wait for it",
        "hq_far_away":    "HQ is too far away",
        "hq_not_found":   "HQ not found",
        "johnes2":        "In 2427 horror. Developers from this intelligence organisation called YEN.NEFER created an AI codenamed NASTASYA. It was supposed to help with weapons transport over time. It was given all the information about the YEN.NEFER network and given a few days to study it. The artificial intelligence learnt too much and decided that ALL humans were like these bandits and unworthy of him helping them. YEN.NEFER gave it too much control at that point. NASTASYA is doing horrible things in 2427. You have to go there. You show up in a random place, find way.",
        "robot1":         "_You are greeted by a very strange robot that dances tectonics without music_",
        "robot2":         "_As you look a little closer, you notice that the robot has wires sticking out in various places. When you look a little more closely, you see that he is full of holes, but they are overgrown with mould with a reddish tinge._",
        "you_mind":       "_Where am I? What's wrong with him?_",
        "guard1":         "_In the distance you saw a guard booth and an exit._",
        "guard2":         "Hey, humanoid!",
        "guard3":         "Who is you? What is happened?",
        "guard4":         "He-He, I'm not letting you out.!",
        "guard5":         "_You saw that there was a small talking hamster on the booth counter_",
        "guard6":         "You want to get out, guess the riddle!",
        "manual2":        "Deepseek will come up with riddles and answers to them. Computer resources may be required. Proceed only if you have installed `deepseek-r1:7b` following the guide in README.md and you have a powerful computer",
        "manual3":        "The computer can explode, so there's only one round here + this bro can make mistakes",
        "guard7":         "Wrong! All right, I'll let you in, you owe me. And the correct answer was {}",
        "guard8":         "That's a great one! Ai-da {}",
        "notification":   "You've received a notification",
        "coord":          "Good afternoon, Agent Scott. Your coordinates - {}-{}",
        "robot_met":      "Along the way, you're met by a robot",
        "artist1":        "I'm a robot artist. I have to paint a picture. A picture.",
        "artist2":        "Hi. Yesterday I was supposed to draw 2 portraits of different people, but I accidentally drew one with two people merged! Help me remember who is in the picture",
        "manual4":        "_Artificial intelligence merged the images of two people into one. Pick a category and write 2 surnames separated by `+`. If the *character* doesn't have a surname (you'll understand this case if you come across one), write the first name_",
        "manual5":        "You have to write the last names of two people separated by `+`",
        "wrong_art":      "Doesn't look like much... How about another one? If you don't know, look at the other portrait.",
        "artist3":        "Yes! It's them! Thank you very much",
        "stableman1":     "Hi! I've trained four horses for the races. Which one do you think I should bet on?",
        "stableman2":     "What the hell kind of advice did you give me?! I'm not gonna let you go now! Unless I win, you're not leaving here.",
        "stableman3":     "Here we go! I like the people I use to make money!",
        "nefer_guards":   "You were attacked by 3 guards. You know what you need to do",
        "nefer1":         "Why did you come here? One of those people trying to eliminate me? Let's play a few games.",
        "nefer2":         "Huh! You don't get it. You just do *NOT* have a choice.",
        "nefer3":         "You are so obedient! I love guys like you",
        "nefer4":         "So, let's get started! We're going to play...",
        "nefer5":         "Tic-Tac-Toe!!!",
        "nefer6":         "You think you can chat? Ha!",
        "nefer7":         "Let's continue to pretend like we were NOT playing a giveaway",
        "nefer8":         "You're not so bad! Good boy! I wouldn't mind scratching your ear.",
        "nefer9":         "Whoever didn't make it in time is too late!",
        "nefer10":        "And I'm the best as always!",
        "nefer11":        "So, here we go! I don't understand the point of this game, but I know that *YOU* people like this game. Let's start!",
        "nefer12":        "What a pity I don't have hands!",
        "nefer13":        "And now for the most interesting part of the game!",
        "nefer14":        "While you were playing, I was collecting data on you! Every emotion you had! Interesting, isn't it? I know where you work, where you lived, and what you did *EVERY SECOND*. I don't leave in my lifetime the people who tried to destroy me.",
        "nefer15":        "Just killing you would be *SOOOOO* boring, and why? Your mates from the gang would come after you. You'd just *never be born*. That's my idea! You have one minute before your time runs out! Sounds weird, but fun! Good-bye.",
        "nefer16":        "_The mechanical arm carries you far out into the street._",
        "nefer17":        "_You've been put down next to that robot. You realise something, but it's too late..._",
        "end":            "Congrats on getting through the game! You spent {}. You can communicate with the Artificial Intelligence helper and NASTASYA. Select who you want to communicate with (only if you have installed the correct ollama model)",
        "changed":        "System prompt has changed. You can talk with AI",
        "choosepr":       "Choose prompt"
    }
}

# Переводы кнопок
buttons = {
    "ru": {
        "start":     "Начать игру",
        "read":      "Прочитать",
        "go":        "Отправиться",
        "go2":       "Идти",
        "go3":       "Идти дальше",
        "agree":     "Согласиться",
        "disagree":  "Отказаться",
        "shoot":     "Стрелять",
        "call":      "Звать бандитов",
        "celebrity": "Знаменитости",
        "change":    "Поменять",
        "call_g":    "Звать охранников",
        "helper":    "Помощник",
        "clear":     "Очистить сессию",
    },
    "en": {
        "start":     "Start the game",
        "read":      "Read it",
        "go":        "Go",
        "go2":       "Go",
        "go3":       "Go on",
        "agree":     "Agree",
        "disagree":  "Disagree",
        "shoot":     "Shoot",
        "call":      "Call bandits",
        "celebrity": "Celebreties",
        "change":    "Change",
        "call_g":    "Call guards",
        "helper":    "Helper",
        "clear":     "Clear session"
    }
}

# Переводы имен персонажей
persons = {
    "ru": {
        "johnes":    "*Агент Джонс (Голографический)*",
        "waiter":    "*Оффициант*",
        "you":       "*Вы*",
        "watch":     "*Часы*",
        "mind":      "*В мыслях*",
        "guard":     "*Охранник*",
        "artist":    "*Художник*",
        "stableman": "*Конюх*",
    },
    "en": {
        "johnes":    "*Agent Johnes (Golographic)*",
        "waiter":    "*Waiter*",
        "you":       "*You*",
        "watch":     "*Watch*",
        "mind":      "*In mind*",
        "guard":     "*Guard*",
        "artist":    "*Artist*",
        "stableman": "*Stableman*"
    }
}

# Стикеры
stickers = {
    "pigeon":    "CAACAgIAAxkBAAEOJBhn39vQjvLL9ULGHLLPwz0YtLlhcQACoG4AAvmhAUst5M-iMSKMyDYE",
    "envelope":  "CAACAgIAAxkBAAEOJTRn4Vvo8zejEbZBOBYFkLrLGgk_UwACsmoAAp23EUvj9WFZmc85YDYE",
    "waiter":    "CAACAgIAAxkBAAEOJURn4WCNhjqlsBnK1bJiqNmQhQqcnAACFmcAAguhCUvCaKv9ReYFdDYE",
    "johnes":    "CAACAgIAAxkBAAEOJuNn4l6Dl2-rNMgUiBtqh4SKOZG_2QAC8m0AAlY9AAFL2HqbUCasTzc2BA",
    "robot":     "CAACAgIAAxkBAAEOJuVn4mMjjWO01Q5jNY876wY7EdavDgACi20AAkplGUvc029kI1XbkzYE",
    "guard":     "CAACAgIAAxkBAAEOJutn4m1BnNlWRtU_VXUCS5ORTMpgkwAC0WMAAnGNEEsGqKvGOxfOtzYE",
    "artist":    "CAACAgIAAxkBAAEOJw9n4pb52lFBa6AFTP-CnpTuHBSS5wACfGoAAhgXEUt6fV2sR5GNzjYE",
    "stableman": "CAACAgIAAxkBAAEOKKNn47uaSr_UuuwI25vFbq7WCN9HXgACLWQAArkPIEs-WiHJk5aRgzYE",
    "nefer":     "CAACAgIAAxkBAAEOKKdn47z_UY0iwzikD42ub1hryFfO6gACR20AAjegCUuW0aXeiV6s_DYE"
}

# Картины художника
artist = {
    "ru": {
        "celeb": {
            "AgACAgIAAxkBAAIChGfiuDxDNa6DooUYekls5ILKX7mBAALt5jEbNfUYS32Lb7u6YNWRAQADAgADeAADNgQ":  ["дуров", "мона лиза"],
            "AgACAgIAAxkBAAICcmfitxn41iWq89CvwDwNgBdf45r6AAJL7DEbfkEQSxupgbXcEM4xAQADAgADeQADNgQ":  ["джоли", "питт"],
            "AgACAgIAAxkBAAEzAfxn4lwyRHBm9cZzwSdvT6ccQMx2zQACUfMxG5L5GEtWT61wfKiEuAEAAwIAA20AAzYE": ["моргенштерн", "бузова"],
            "AgACAgIAAxkBAAEy_hRn4a9C18hiDBSVzA2ijTcnVDV1oQACtfQxG4fYEEtLXrvJ7vLNFAEAAwIAA20AAzYE": ["трамп", "маск"],
            "AgACAgIAAxkBAAICdGfit6bYxpI3SAa6oPVuf3TpLg2WAAJN7DEbfkEQSx-4OEqQbmo5AQADAgADeAADNgQ":  ["месси", "ревва"],
            "AgACAgIAAxkBAAEzAgZn4ly0HKD10Yx93Zb4I9uRq-Y_NAACMvMxG5L5GEulg6llbESBOwEAAwIAA3gAAzYE": ["роналду", "киркоров"],
            "AgACAgIAAxkBAAEzAjFn4mThw6e-Sdcn4Q4WfePDm9j7XwAClPMxG5L5GEtr2diK-AcqZwEAAwIAA20AAzYE": ["харламов", "мусагалиев"],
            "AgACAgIAAxkBAAICmGfiuk6AiieO0krlwFUKsWEfk_9JAALz5jEbNfUYS6AJG-gbiOymAQADAgADbQADNgQ":  ["харламов", "пушкин"],
            "AgACAgIAAxkBAAEzBfBn4s3YRW7s0Iby9w4DBfynkMOIGQAC1uwxGzfUGEupoHRliZfitAEAAwIAA3kAAzYE": ["лепс", "джексон"]
        },
        "funcode": {
            "AgACAgIAAxkBAAICuGfivCx74oPOYO6trStXGGPUdyRZAAIC5zEbNfUYS1pflje1XMU1AQADAgADeAADNgQ":  ["лашко", "беляй"] # мое любимое
        }
    },
    "en": {
        "celeb": {
            "AgACAgIAAxkBAAIChGfiuDxDNa6DooUYekls5ILKX7mBAALt5jEbNfUYS32Lb7u6YNWRAQADAgADeAADNgQ":  ["durov", "mona lisa"],
            "AgACAgIAAxkBAAICcmfitxn41iWq89CvwDwNgBdf45r6AAJL7DEbfkEQSxupgbXcEM4xAQADAgADeQADNgQ":  ["jolie", "pitt"],
            "AgACAgIAAxkBAAEzAfxn4lwyRHBm9cZzwSdvT6ccQMx2zQACUfMxG5L5GEtWT61wfKiEuAEAAwIAA20AAzYE": ["morgenshtern", "buzova"],
            "AgACAgIAAxkBAAEy_hRn4a9C18hiDBSVzA2ijTcnVDV1oQACtfQxG4fYEEtLXrvJ7vLNFAEAAwIAA20AAzYE": ["trump", "musk"],
            "AgACAgIAAxkBAAICdGfit6bYxpI3SAa6oPVuf3TpLg2WAAJN7DEbfkEQSx-4OEqQbmo5AQADAgADeAADNgQ":  ["messi", "revva"],
            "AgACAgIAAxkBAAEzAgZn4ly0HKD10Yx93Zb4I9uRq-Y_NAACMvMxG5L5GEulg6llbESBOwEAAwIAA3gAAzYE": ["ronaldu", "kirkorov"],
            "AgACAgIAAxkBAAEzAjFn4mThw6e-Sdcn4Q4WfePDm9j7XwAClPMxG5L5GEtr2diK-AcqZwEAAwIAA20AAzYE": ["harlamov", "musagaliev"],
            "AgACAgIAAxkBAAICmGfiuk6AiieO0krlwFUKsWEfk_9JAALz5jEbNfUYS6AJG-gbiOymAQADAgADbQADNgQ":  ["harlamov", "pushkin"],
            "AgACAgIAAxkBAAEzBfBn4s3YRW7s0Iby9w4DBfynkMOIGQAC1uwxGzfUGEupoHRliZfitAEAAwIAA3kAAzYE": ["leps", "jakson"]
        },
        "funcode": {
            "AgACAgIAAxkBAAICuGfivCx74oPOYO6trStXGGPUdyRZAAIC5zEbNfUYS1pflje1XMU1AQADAgADeAADNgQ": ["lashko", "belyai"] # moye lyubimoe
        }
    }
}
