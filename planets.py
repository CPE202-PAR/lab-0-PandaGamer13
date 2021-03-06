# Given earth weight and planet, returns weight on provided planet
# If string does not match a planet, raise ValueError
def weight_on_planets(pounds: float, planet: str) -> float:
   weight = 0.0
   if planet == "Mars":
      weight = pounds * 0.38

   elif planet == "Jupiter":
      weight = pounds * 2.34

   elif planet == "Venus":
      weight = pounds * 0.91

   else:
      raise ValueError()
   
   return weight

if __name__ == '__main__':    # pragma: no cover
   pounds = float(input("What do you weigh on earth? "))
   print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
          "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.\n"+
          "On Venus you would weigh", weight_on_planets(pounds, "Venus"),"pounds.")
