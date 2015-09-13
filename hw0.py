def countScotch():
  data = open('/home/azureuser/hw0/iowa-liquor-sample.csv', 'r')
   
  count = 0

  for line in data:
    if "single malt scotch" in line.lower():
      count = count + 1

  return count

if __name__ == '__main__':
  print(countScotch())
