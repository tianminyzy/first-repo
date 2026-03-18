import random
'''def fortune():
  yun = ['Don\'t pursue happiness – create it.',
        'All things are difficult before they are easy.',
        'The early bird gets the worm, but the second mouse gets the cheese.',
        'Someone in your life needs a letter from you.',
        'Don\'t just think. Act!',
        'Your heart will skip a beat.',
        'The fortune you search for is in another cookie.',
        'Help! I\'m being held prisoner in a Chinese bakery!']
  print(yun[random.randint(0,len(yun)-1)])''' # 初级写法
def fortune():
    yun = ['Don\'t pursue happiness – create it.',
           'All things are difficult before they are easy.',
           'The early bird gets the worm, but the second mouse gets the cheese.',
           'Someone in your life needs a letter from you.',
           'Don\'t just think. Act!',
           'Your heart will skip a beat.',
           'The fortune you search for is in another cookie.',
           'Help! I\'m being held prisoner in a Chinese bakery!']
    print(random.choice(yun)) # random.choice 随机从列表选
fortune()
