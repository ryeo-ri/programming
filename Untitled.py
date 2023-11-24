import log
from mastodon import Mastodon, StreamListener
from collections import defaultdict
from oauth2client.service_account import ServiceAccountCredentials
import requests
import gspread
import time
import random
import re
import ssl

#마스토돈 접근
mastodon = Mastodon(
    api_base_url  = 'https://occm.cc/',
    client_id     = 'u-N2Ulkveqf4kLdkec3OaccXElzoaAwTcUl5LnNAaI0',
    client_secret = '3WmIEljVOXs4uE_ns4LSXZh0lVBRr31bBEMJG3n7q_c',
    access_token  = 'KazgmsAR1VlNWA0qkKDd8B-BVUpyfaBhZWESlBn2dFU'
)
#구글 연동
gc = gspread.service_account()
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/10idqD6N4qPv-CCh01bx1-nc6wbcaCB9NlACjb99xD1w/edit?usp=sharing')
# 구글 인증 정보
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("/home/ubuntu/auth/service_account.json", scope)
client = gspread.authorize(creds)


# 로그
logger = log.get_logger()
notif = mastodon.notifications() # 알림을 가져옵니다.
count = 0

class Stream(StreamListener):
    def __init__(self): #상속
        super(Stream, self).__init__()

    def on_notification(self,notif): # 알림이 왔을 때 호출
        if notif['type'] == 'mention': # 알림의 내용이 멘션인지 확인
            content = notif['status']['content'] # 답장 
            id = notif['status']['account']['username'] #아이디 
            st = notif['status']
            name = notif['status']['account']['display_name'] # 닉네임
            main(content,st,id,name)
                 

def main(content,st,id,name):
    req = content.rsplit(">")[-2].split("<")[0].strip() #들어온 본문 
    resr = None
    sheet = client.open('bot-data-example') #시트 제목입력
    luck_data = sheet.worksheet('운세')
    member_data = sheet.worksheet('멤버리스트')
    cooking_data = sheet.worksheet('요리')
    play_data = sheet.worksheet('조사')
    event_data = sheet.worksheet('조사2')
    shop_data = sheet.worksheet('가챠')
    dog_data = sheet.worksheet('도감')  
    mandara_data = sheet.worksheet('만다라') 
    
    keyword = play_data.row_values(1) #키워드 조사
    for col_index, value in enumerate(keyword):#print(f"Index: {col_index}, Value: {value}")
        if value in content:
            cell = play_data.find(value)
            text_list = play_data.col_values(cell.col)[1:] # 첫 행은 제외 #열값을 가져옴
            resr = f"{random.choice(text_list)}"
            break # 값을 찾았으면 루프를 종료합니다.
    
    if '[가챠]' in content:
            text_list = shop_data.col_values(1)[1:] # 첫 행은 제외 #열값을 가져옴
            resr = f"{random.choice(text_list)}"  
            
    if '[열챠]' in content:
            text_list = shop_data.col_values(1)[1:] # 첫 행은 제외 #열값을 가져옴
            resr = f"\n{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n" + f"{random.choice(text_list)} \n"

    if '[낚시]' in content:
        text_list = shop_data.col_values(3)[1:] # 첫 행은 제외 #열값을 가져옴
        resr = "'{}'을(를) 낚았다!".format(random.choice(text_list)) 

    if '[지목]' in content:
            text_list = shop_data.col_values(2)[1:] # 첫 행은 제외 #열값을 가져옴
            resr = f"{random.choice(text_list)}"  
            
    if '[동인지]' in content:
            text_list = shop_data.col_values(2)[1:] # 첫 행은 제외 #열값을 가져옴
            text_list2 = event_data.col_values(6)[1:] # 첫 행은 제외 #열값을 가져옴
            resr = f"「{random.choice(text_list)}" + " x " + f"{random.choice(text_list)}」이(가) 그려진 책을 받았다. 마지막 페이지에 후기가 작성되어 있다.\n" + f"{random.choice(text_list2)}"              

    if '[재료박스]' in content:
            text_list = shop_data.col_values(3)[1:] # 첫 행은 제외 #열값을 가져옴
            resr = "상자를 열였다. 들어있는 것은 ...\n" + f"{random.choice(text_list)} / " + f"{random.choice(text_list)} / " + f"{random.choice(text_list)} / "+ f"{random.choice(text_list)}"  

    if '[운세]' in content:
        #C열의 내용을 ','로 구분하여 각각의 문장으로 가져옵니다.
        text_list= str(luck_data.col_values(3)).split(',') 
        user_dict = mastodon.account_verify_credentials()
        resr = name +"님의 오늘의 운세 " + "{}".format(random.choice(text_list)) 

    if '1d2' in content:
        resr = str(random.randint(1,2))

    if '1D2' in content:
        resr = str(random.randint(1,2))
        
    if '1d10' in content:
        resr = str(random.randint(1,10)) 

    if '1D10' in content:
        resr = str(random.randint(1,10))       
        
    if '1d20' in content:
        resr = str(random.randint(1,20)) 

    if '1D20' in content:
        resr = str(random.randint(1,20))       
        
    if '1d100' in content:
        resr = str(random.randint(1,100))

    if '1D100' in content:
        resr = str(random.randint(1,100))      
        
    if 'yn' in content:
        resr = str(random.choice(["Y", "N"]))
        
    if 'YN' in content:
        resr = str(random.choice(["Y", "N"])) 
        
    if '[복권추첨]' in content:
        resr = "\n☞당첨번호☜\n [" + str(random.randint(0,44)) + "] " + "[" + str(random.randint(0,44)) + "] "+ "[" + str(random.randint(0,44)) + "] "
        +"[" + str(random.randint(0,44)) + "] "+ "[" + str(random.randint(0,44)) + "] "+ "[" + str(random.randint(0,44)) + "]"
        
    if '[요정우유]' in content: 
        cell = member_data.find(id)
        print("%s행 %s열에서 찾았습니다." % (cell.row, cell.col))
        delta = 1 #증가시킬 숫자
        for i in range(1, 9): #시트 내 인식할 범위. 0부터 시작합니다. 제 시트의 경우 '아이디' 열부터 '출석'열까지 인식시켰습니다.
            print(member_data.cell(cell.row, i).value, end=' ')
            if i == 6: # 횟수 감산 열
                times = int(member_data.cell(cell.row, i).value) #횟수 감산 열 가져오기
                if times == 0: # 요정 횟수가 0회인 경우
                    member_data.update_cell(cell.row, i, times + delta)
                    resr = "[147] 요정우유를 먹이자 새끼 손톱 크기였던 아기 요정은 순식간에 검지 반 토막 만큼 자라났다. 고맙다 말하고 싶은 걸까? 당신의 주변을 활기차게 날아다닌다. 요정은 당신을 조금 더 사랑하게 됐다."
                elif times == 1: # 요정 횟수가 1회인 경우
                    member_data.update_cell(cell.row, i, times + delta)
                    resr = "[147] 요정우유를 먹이자 아기 요정을 덮은 생선이 먹음직스럽게 두툼해졌다. '초.' 예전에 비하면 말수가 줄어든 것 같기도... 요정은 조금 더 어른스러워졌다. "
                elif times == 2: # 요정 횟수가 2회인 경우
                    member_data.update_cell(cell.row, i, times + delta)
                    resr = "완전히 자라버린 요정은 부쩍 잘 움직이지 않게 됐다. 마치 평범한 초밥 같은 모습... 하지만 이 초밥은 당신의 손이 닿는 한 언제까지고 따듯한 온기를 지닐 것이다. 요정이 정말로 존재한다면 어째서 지금까지는 만날 수 없었을까? 어쩌면 우리가 어른이 되기 이전에 요정들도 아주 빠른 성장을 거치기 때문인지도 모르겠다." 
                elif times == 3: # 요정 횟수가 3회인 경우
                    member_data.update_cell(cell.row, i, 0) # 자신의 열값을 0으로 되될림
                    resr = "[147] 요정우유를 먹이자 새끼 손톱 크기였던 아기 요정은 순식간에 검지 반 토막 만큼 자라났다. 고맙다 말하고 싶은 걸까? 당신의 주변을 활기차게 날아다닌다. 요정은 당신을 조금 더 사랑하게 됐다."
                    for j in range(1, 9): # 같은 행에 있는 다른 열의 값 변경
                        if j == 4: # 자신의 열이 아닌 경우
                            other_value = int(member_data.cell(cell.row, j).value) # 다른 열의 값 가져오기
                            member_data.update_cell(cell.row, j, other_value + delta) # 다른 열의 값을 1 상승시킴

 
    #중괄호를 쓰는 키워드             
    if '{' in content and '}' in content:
        event = event_data.col_values(1)[1:]
        print(event)
        for col_index, value in enumerate(event):
            print(f"Index: {col_index}, Value: {value}")
            if value in content:
                #판정 요구치
                demand = event_data.row_values(col_index+2)
                print(demand)
                #멘션으로 받은 숫자 
                content = content.replace(" ", "")    
                match = re.search("{(\d+)}", content)
                #값비교
                if int(match.group(1)) >= int(demand[1]):
                    resr = "{}".format(demand[2]) #성공 
                else:
                    resr = "{}".format(demand[3]) #실패        
                    break 
                #입력된 중괄호 안의 값을 가져옴
                #중괄호 안의 값과 두번째 셀을 비교함
                #비교한 후 성공하면 3번째 셀을 실패하면 4번째 셀을 불러옴 
            
    #요리
    if '[요리]' in content:
        content = content.replace(" ", "")
        cook = re.search("{(.+?)}", content) #중괄호 안에 있는 데이터 뽑음
        if cook:
            ingredients = cook.group(1).split(",")
        recipes = []
        for row in cooking_data.get_all_values()[1:]: # 첫 번째 행 제외
            recipe_name = row[0]
            recipe_ingredients = row[1].split(",") # 재료들을 쉼표로 구분하여 리스트로 변환
            recipe_data = row[2]
            if sorted(ingredients) == sorted(recipe_ingredients):
                recipes.append(recipe_name)
                recipes.append(recipe_data)
                print("원래재료"+ str(ingredients) + "// 레시피재료" + str(recipe_ingredients) +"// 결과"+ str(recipe_name))
        if len(recipes) > 0:
            resr = "'{}'이(가) 만들어졌다! ".format(recipes[0]) + "{}".format(recipes[1])
        else:
            resr = "'[69] 개밥'이 만들어졌다. 개밥으로 주자." 
            
      #사료공양
    if '[사료공양]' in content:
        match = re.search("{(.+?)}", content)  # 중괄호 안에 있는 데이터 뽑음
        dog = ['케르', '베로', '스']
        random_dog = random.choice(dog)
        if match:
            search_data = match.group(1)

        found_rows = []
        for row in dog_data.get_all_values()[1:]:  # 첫 번째 행 제외
            if search_data in row:
                        found_rows.append(row)
        if len(found_rows) > 0:
            resr = ""
            for row in found_rows:
                resr = "\n{}가 ".format(random_dog) + "[{}]".format(row[0]) + " {}을(를) 뱉어냈다.".format(row[2])
        else:
            resr = "눈 앞의 악마는 재료의 이름을 확인하라고 말하고 있다..."   
        
        #만다라
    if '[만다라]' in content:
        content = content.replace(" ", "")
        match = re.search("{(.+?)}", content)  # 중괄호 안에 있는 데이터 뽑음
        count = [1, 3, 5]
        up_point = random.choice(count)
        found_rows = []
        if match:
            search_value = match.group(1)    
            
        for row in mandara_data.get_all_values()[1:]:  # 첫 번째 행 제외
            if search_value in row[1]:  # 두 번째 열의 값 비교
                found_rows.append(row)

        if len(found_rows) > 0:
            resr = ""
            for row in found_rows:
                current_value = mandara_data.cell(2, 1).value
                new_value = int(current_value) + up_point

                if new_value >= 99:
                    resr += "‘[150] 세계평화’이(가) 만들어졌다! \n한 그릇에 수많은 재료들이 어우러져 있다. 전혀 어울리지 않는 재료라고 생각되어도 만나보지 않으면 모르는 법. 독특한 조합은 새로운 맛의 발견을 이끌기 마련이다. 한입 먹어보면 익숙한 사람들의 얼굴이 스쳐 지나간다. 요리를 만든 사람의 마음이 느껴지는 맛은 마음을 평화롭게 만들어 준다."
                else:
                    mandara_data.update_cell(2, 1, new_value)
                    resr = "\n가마솥 앞의 '{}'이(가) 당신에게 인사한다. ".format(row[1]) + "{}".format(row[2])  + "\n마음이 {} 차오른다.".format(up_point) +" [완성도 {}]".format(new_value)
        else:
            resr = "레시피의 재료는 마음이 담긴 만다라! 다른 재료를 넣어선 안된다."
            
            
            
    # 멘션달기
    if resr != None :
        # 로그 
        
        print(name + " @" + id + " / "+ req +" / "+ resr) 
        print(content)
        log_resr = resr.replace("\n", "")
        logger.info(name + " @" + id + " / "+ req +" / "+ log_resr)        
        return mastodon.status_reply(st,resr,id, visibility='unlisted')


# 답변되지 않은 알림 답변기능
while True: 
    try:
        if notif[count]['type'] == 'mention':
            if notif[count]['status']['replies_count'] == 0:
                content = notif[count]['status']['content']
                id = notif[count]['status']['account']['username']
                st = notif[count]['status']
                name = notif[count]['status']['account']['display_name']
                main(content, st, id, name)
                count += 1
            else:
                break
        else:
            count += 1
        count += 1
    except IndexError:
        break

mastodon.stream_user(Stream()) # 스트림 시작