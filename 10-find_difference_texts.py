"""Found the difference between two texts"""

text1 = 'exposes a problem with free speech and online media. Today, with the expand of "technological sphere", anyone can publish anything and based on the free speech, the regulation seem impossible. This problem has been shown in Donald Trump case against Twitter. In fact, president Trump has been banned from the Twitter\'s platform because he published "fake news" about the presidential election and this fakes news created a mob of this supporter who stormed the Capitol. In order to stop that, Twitter\'s banned Donald Trump for encouragement of violence. This case exposes a normative conflict: free speech against freedom of contract. Indeed, Twitter\'s term and service stat that the platform can delete any profile at any time without a justification or appeal process'
text2 = 'Exposes a problem with free speech and online media. Today, with the expand of "technological sphere", anyone can publish anything and based on the free speech, the regulation seem impossible. This problem has been show in Donald Trump case angainst Twitter. In fact, president Trump has been banned from the Twitter\'s plateform because he published "fake news" about presidential election and this fakes news created a mob of this supporter who stormed the Capitol. \nIn order to stop that, Twitter\'s banned Donald Trump for encouragement of violence. This case expose a normative conflict : free speech against freedom of contrat. Indeed, Twitter\'s term and service stat that the plateform can delete any profil at any time without an justification or appel process'

# text1 = 'exposes a problem with free and online media.'
# text2 = 'Exposes a problem with fre online media'
a = text1.replace("\n","").split(" ")
b = text2.replace("\n","").split(" ")
Text1_aa = 0
text2_bb = 0
for i in range(0,len(a)):
    tab = [None, None, None, None]  # text1 = None,None,# text2 = None,None
    if Text1_aa < len(a):
        tab[0]=a[Text1_aa]
        if Text1_aa +1 < len(a):
            tab[1] = a[Text1_aa+1]

    if text2_bb < len(b):
        tab[2]=b[text2_bb]
        if text2_bb + 1 < len(b):
            tab[3] = b[text2_bb+1]

    if tab[0] != tab[2]:
        if tab[0] == tab[3]:
            print(tab[0],'**aaa**',tab[2],tab[3])
            text2_bb = text2_bb + 1
        elif tab[1] == tab[2]:
            print(tab[0],tab[1],'**bbb**', tab[2])
            Text1_aa = Text1_aa + 1
        else:
            print(tab[0],tab[2])

    Text1_aa = Text1_aa + 1
    text2_bb = text2_bb + 1
