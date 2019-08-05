def convert(number):
    soundPairs = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    raindrops = [sound for factor, sound in soundPairs if number%factor == 0]
    if len(raindrops) == 0:
      return str(number)
    else:
      return "".join(raindrops)

