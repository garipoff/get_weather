import pyowm
import plotly.graph_objects as go

owm = pyowm.OWM('API')

print('Введите координаты в целочисленном типе')
a=int(input('Широта:'))
b=int(input('Долгота:'))
print('Ждите...')
temp = []

for i in range(a-4,a+4,2):
    for j in range(b-4,b+4,2):
        obs = owm.weather_at_coords(i, j)
        w = obs.get_weather()
        t = w.get_temperature('celsius')
        temp.append(t['temp'])        

t = [temp[idx:idx + 5] for idx in range(0, len(temp), 5)]
print('Готово')

fig = go.Figure(data =
    go.Contour(
        z=t,
        x=[b-4, b-2],
        y=[a-4, a-2],
        connectgaps=True,        
    )
)
fig.show()
