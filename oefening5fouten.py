def genereerLabels(verzameling, deelverzamelingEven, deelverzamelingOneven):
  labels = set()
  getalOneven = 1
  getalEven = 2
  for x in verzameling:
    if x in deelverzamelingEven:
      labels.add(str(getalEven) + " " + x)
      getalEven += 1
    else:
      labels.add(str(getalOneven) + " " + x)
      getalOneven += 1
  return labels


def genereerLabels(verzameling, deelverzamelingEven, deelverzamelingOneven):
labels = set()
getal = 1
for x in verzameling:
  if x in deelverzamelingEven:
    labels.add(str(getal) + " " + x)
    getal += 2
  else:
    labels.add(str(getal) + " " + x)
    getal += 2
return labels

