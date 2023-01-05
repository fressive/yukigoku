# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("？？？")
define yk = Character("叶子")
define s = Character('站长')
define m = Character('岛村')

# 游戏在此开始。

label start:

    play sound "audio/sound_train_02.mp3" volume 0.75

    "穿过县界长长的隧道，便是雪国。"

    "夜空下一片白茫茫。火车在信号所前停了下来。"

    scene main bg 
    with Fade(0.5, 0.0, 0.5)

    "一位姑娘从对面座位上站起身子，把我座位前的玻璃窗打开。"

    "一股冷空气卷袭进来。姑娘将身子探出窗外，仿佛向远方呼唤似地喊道："

    voice 'audio/voice_yk_001.mp3'
    e "「站长先生，站长先生！」"

    voice 'audio/voice_yk_002.mp3'
    show yk normal 01 with dissolve:
        zoom 1.2
        xpos 300
        ypos 120
    play music 'audio/bgm 001.mp3'
    e "「站长先生，是我。您好啊！」"

    s "「哟，这不是叶子姑娘吗！回家呀？又是大冷天了。」"

    voice 'audio/voice_yk_003.mp3'
    yk "「听说我弟弟到这里来工作，我要谢谢您的照顾。」"

    s "「在这种地方，早晚会寂寞得难受的。年纪轻轻，怪可怜的！」"

    voice 'audio/voice_yk_004.mp3'
    yk "「他还是个孩子，请站长先生常指点他，拜托您了。」"

    s "「行啊。他干得很带劲，往后会忙起来的。」"
    s "「去年也下了大雪，常常闹雪崩，火车一抛锚，村里人就忙着给旅客送水送饭。」"

    voice 'audio/voice_yk_005.mp3'
    yk "「站长先生好像穿得很多，我弟弟来信说，他还没穿西服背心呢。」"
    
    s "「我都穿四件啦！小伙子们遇上大冷天就一个劲儿地喝酒，现在一个个都得了感冒，东歪西倒地躺在那儿啦。」"

    "站长向宿舍那边晃了晃手上的提灯。"

    voice 'audio/voice_yk_006.mp3'
    yk "「我弟弟也喝酒了吗？」"

    s "「这倒没有。」"

    voice 'audio/voice_yk_007.mp3'
    yk "「站长先生这就回家了？」"

    s "「我受了伤，每天都去看医生。」"

    voice 'audio/voice_yk_008.mp3'
    yk "「啊，这可太糟糕了。」"

    "和服上罩着外套的站长，在大冷天里，仿佛想赶快结束闲谈似地转过身来说："

    s "「好吧，路上请多保重。」"

    voice 'audio/voice_yk_009.mp3'
    yk "「站长先生，我弟弟还没出来吗？」"

    "叶子用目光在雪地上搜索。"

    voice 'audio/voice_yk_010.mp3'
    yk "「请您多多照顾我弟弟，拜托啦。」"

    "她的话声优美而又近乎悲戚。那嘹亮的声音久久地在雪夜里回荡。 "

    "火车开动了，她还没把上身从窗口缩回来。"
    "一直等火车追上走在铁路边上的站长，她又喊道："

    voice 'audio/voice_yk_011.mp3'
    yk "「站长先生，请您告诉我弟弟，叫他下次休假时回家一趟！」"

    s "「行啊！」"
    "站长大声答应。 "

    "叶子关上车窗，用双手捂住冻红了的脸颊。 "

    return
