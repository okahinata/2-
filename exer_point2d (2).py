
"""
学籍番号： F222014
氏名 ：   岡　日那汰
"""

# ２次元座標クラス

#ここからプログラム書く

class Point2D:
    def __init__(self,posX,posY) :
        self._posX=posX
        self._posY=posY

    def get_x(self):
        return self._posX
    
    def get_y(self):
        return self._posY
    
    def set_x(self,x):
        self._posX=x
    
    def set_y(self,y):
        self._posY=y

    
kazu=int(input('管理する2次元座標の数を入力してください：'))
if kazu<1: 
    print('１以上の数を入力してください')
    exit()
coordinates=[]
for i in range(1,kazu+1):
    print(i,'つ目のx座標を入力してください:',end='') 
    pointx=int(input(''))
    print(i,'つ目のy座標を入力してください:',end='')  
    pointy=int(input(''))
    coordinate=Point2D(pointx,pointy)
    coordinates.append(coordinate)

order=int(input('出力したい２次元座標の番号を入力してください：'))
if kazu<order:
    print('入力数を超えています')
    exit()
if order<=0:
    print('１以上を入力してください')
    exit()
out_coordinate=coordinates[order-1]

print(order,'つ目の２次元座標は（',out_coordinate.get_x(),',',out_coordinate.get_y(),')です。')
# 出力結果
"""
管理する2次元座標の数を入力してください：3
1 つ目のx座標を入力してください:1
1 つ目のy座標を入力してください:2
2 つ目のx座標を入力してください:3
2 つ目のy座標を入力してください:4
3 つ目のx座標を入力してください:5
3 つ目のy座標を入力してください:6
出力したい２次元座標の番号を入力してください：1
1 つ目の２次元座標は（ 1 , 2 )です。

"""
