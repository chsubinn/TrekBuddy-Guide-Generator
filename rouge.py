from rouge import Rouge

model_out = ["광화문은 서울특별시 종로구의 조선왕조 법궁인 경복궁의 남쪽에 있는 정문이다. 임금의 큰 덕(德)이 온 나라를 비춘다는 의미이다. 광화문 앞에는 지금은 도로 건설로 사라진 월대가 자리잡고 있었으며, 양쪽에는 한 쌍의 해태 조각상이 자리잡고 있다. 광화문의 석축부에는 세 개의 홍예문이 있다. 가운데 문은 임금이 다니던 문이고, 나머지 좌우의 문은 신하들이 다니던 문이었는데, 왼쪽 문은 무신이, 오른쪽 문은 문신이 출입했다."]

reference = ["광화문은 조선왕조법궁인 경복궁의 남쪽에 있는 정문으로, 임금의 큰 덕(德)이 온 나라를 비춘다는 의미이다. 경복궁의 정전인 근정전으로 가기 위해 지나야 하는 문 3개 중에서 첫째로 마주하는 문이다. 광화문 앞 양쪽에는 한 쌍의 해태 조각상이 자리잡고 있다. 광화문의 석축부에는 세 개의 홍예문이 있는데, 가운데 문이 임금이, 나머지 좌우의 문이 신하들이 다니던 문이다."]
rouge = Rouge()

print(rouge)

print(rouge.get_scores(model_out, reference, avg=True)['rouge-1'])
print(rouge.get_scores(model_out, reference, avg=True)['rouge-2'])
print(rouge.get_scores(model_out, reference, avg=True)['rouge-l'])


