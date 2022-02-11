# Расчет награды за просмотр рекламы
from colorama import init
from colorama import Fore, Back, Style
init()

adsRewardInitial = 800
adsRewardPerRank = 1200
adsRankDivider = 10
print (Back.CYAN)
rank = input( "Введите ранг игрока: ")

rewardSilver = ( int(rank) // adsRankDivider * adsRewardPerRank + adsRewardInitial)
print (Back.GREEN)
print ("Награда за просмотр рекламы составит: " + str(rewardSilver) + " серебра" )

input ()