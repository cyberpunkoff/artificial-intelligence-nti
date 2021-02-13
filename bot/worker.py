import random

programming = [{'link': 'https://habr.com/ru/company/crossover/blog/351884/', 'rating': 17, 'lenght': 115}, {'link': 'https://habr.com/ru/post/151802/', 'rating': 7, 'lenght': 126}, {'link': 'https://habr.com/ru/company/intel/blog/477476/', 'rating': 7, 'lenght': 18}, {'link': 'https://habr.com/ru/post/247363/', 'rating': 23, 'lenght': 118}, {'link': 'https://habr.com/ru/post/475404/', 'rating': 11, 'lenght': 25}, {'link': 'https://habr.com/ru/post/476100/', 'rating': 14, 'lenght': 24}, {'link': 'https://habr.com/ru/company/JetBrains-education/blog/477898/', 'rating': 14, 'lenght': 75}, {'link': 'https://habr.com/ru/company/it-grad/blog/418909/', 'rating': 14, 'lenght': 42}, {'link': 'https://habr.com/ru/post/143716/', 'rating': 58, 'lenght': 20}, {'link': 'https://habr.com/ru/post/50873/', 'rating': 32, 'lenght': 32}]
security = [{'link': 'https://habr.com/ru/company/microsoft/blog/477384/', 'rating': 6, 'lenght': 22}, {'link': 'https://habr.com/ru/company/aladdinrd/blog/413631/', 'rating': 10, 'lenght': 22}, {'link': 'https://habr.com/ru/company/jetinfosystems/blog/423477/', 'rating': 28, 'lenght': 38}, {'link': 'https://habr.com/ru/news/t/460639/', 'rating': 10, 'lenght': 10}, {'link': 'https://habr.com/ru/company/jetinfosystems/blog/427263/', 'rating': 20, 'lenght': 22}]
ai_and_data = [{'link': 'https://habr.com/ru/news/t/476080/', 'rating': 11, 'lenght': 21}, {'link': 'https://habr.com/ru/company/pt/blog/321586/', 'rating': 23, 'lenght': 159}, {'link': 'https://habr.com/ru/company/jetinfosystems/blog/471626/', 'rating': 29, 'lenght': 115}, {'link': 'https://habr.com/ru/post/484150/', 'rating': 33, 'lenght': 26}, {'link': 'https://habr.com/ru/company/madrobots/blog/442866/', 'rating': 9, 'lenght': 30}, {'link': 'https://habr.com/ru/company/jetinfosystems/blog/475862/', 'rating': 13, 'lenght': 57}, {'link': 'https://habr.com/ru/news/t/483620/', 'rating': 13, 'lenght': 33}]

def recommend(prefered, stype, longness):
    candidates = []
    lenght = 0
    # for cantidate in locals().get(prefered):
        # if stype == "casual" and candidat["rating"] >= 550:
           # candidates.update(cantidate)
        # if stype == "usual" and  400 <= candidat["rating"] <= 550:
            # candidates.update(cantidate)
        # if stype == "unusual" and  80 <= candidat["rating"] <= 200:
            # candidates.update(cantidate)
    
    random.shuffle(programming)
    random.shuffle(security)
    random.shuffle(ai_and_data)
    
    for cantidate in globals().get(prefered):
        candidates.append(cantidate)
        
    for cantidate in candidates:
        lenght += cantidate["lenght"]
        
    m_lenght = lenght/len(candidates)
    for cantidate in candidates:
    
        if longness == "lower" and cantidate['lenght'] < m_lenght:
            return cantidate["link"]
        if longness == "higer" and cantidate['lenght'] > m_lenght:
            return cantidate["link"]
