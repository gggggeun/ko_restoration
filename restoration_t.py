from restoration import main

mecab, complex_verb_set = main.set_env()

lines = ['안녕하세요. 만나뵙게 되어서 반갑습니다. 오늘은 강릉에서 이벤트가 있을 계획입니다. 모두 시간과 장소를 유의하여 늦지 않도록 조심해주시길 바랍니다.','테스트 확인 중 입니다.']
print("원형 복원 전 : \n", lines)
result = main.start_restoration(mecab, complex_verb_set, lines)
print("원형 복원 후 : \n ", result)
