# 参考
# folium: official github
# https://github.com/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb 
# https://python-visualization.github.io/folium/quickstart.html#Getting-Started
# python folium で、都内の公園にまつわる情報を地図上に描画する
# https://www.monotalk.xyz/blog/python-folium-%E3%81%A7%E9%83%BD%E5%86%85%E3%81%AE%E5%85%AC%E5%9C%92%E3%81%AB%E3%81%BE%E3%81%A4%E3%82%8F%E3%82%8B%E6%83%85%E5%A0%B1%E3%82%92%E5%9C%B0%E5%9B%B3%E4%B8%8A%E3%81%AB%E6%8F%8F%E7%94%BB%E3%81%99%E3%82%8B/
# Qiita: Folium: Pythonでデータを地図上に可視化
# https://qiita.com/nanakenashi/items/824c0cb16860ca59a424
# Folium: Python で地図可視化
# https://takaishikawa42.hatenablog.com/entry/2019/01/11/234716

# Folium: error
# https://github.com/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb


# ###
# # foliumの動作はどうやらgeojsonの形式に大きく依存するらしい
# # folium公式に合わせるように柔軟にgeojsonの値を変えられるようなスクリプトが必要
# folium 0.10.1 + 公式us-states.jsonを試した
# 正常に動作

# folium 0.10.1 + tokyo.jsonを試した
# tokyo.json内のcodeを文字列に変えた
# 動きはするが、地図上（カラー）に値は反映されず、すべてにnanが入っていた（nan_fill_colorで確認）

# folium 0.8.3 + tokyo.jsonを試した pip3 install folium==0.8.3
# folium 0.10.1と同様の結果

# folium 0.10.1 + tokyo23.jsonを試した
# tokyo.jsonと同様の結果

# folium 0.8.3 + tokyo23.jsonを試した
# 正常に動作した
# ####


import folium
import pandas as pd
import datetime
from folium import Map, LayerControl, Choropleth

addedcode_tokyo_cases = "../data/addedcode_tokyo_" + datetime.date.today().strftime("%Y_%m_%d") + ".csv"
print(addedcode_tokyo_cases)

def main():

    # tokyo_geo = '../tokyoGeoJson/tokyo.json'
    tokyo_geo = '../JapanCityGeoJson/geojson/13/tokyo23.json'
    tokyo_data = pd.read_csv(addedcode_tokyo_cases)
    tokyo_data['Municipality_code'] = tokyo_data['Municipality_code'].astype(str)
    tokyo_data['Num_cases'] = tokyo_data['Num_cases'].astype(int)
    # print(tokyo_data[['Municipality_code', 'Num_cases']])

    # m = folium.Map(location=[48, -102], zoom_start=3)

    # 東京都港区芝公園を設定
    tokyo23_location = [35.658593, 139.745441]
    # m = folium.Map(location=tokyo23_location,
    #                tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}.png',
    #                attr='OpenStreetMap',
    #                zoom_start=11)
    m = Map(location=tokyo23_location,
                tiles='cartodbpositron',
                attr='OpenStreetMap',
                zoom_start=11)


    choropleth = Choropleth(
        geo_data=tokyo_geo,
        data=tokyo_data,
        columns=['Municipality_code', 'Num_cases'],
        # key_on='feature.properties.code',
        key_on='feature.id',
        name='choropleth',  
        fill_opacity=0.7,
        line_opacity=0.2,
        # line_color='red',
        fill_color='OrRd',
        # bins=[0, 100, 200, 300, 400, 500]
        # nan_fill_color="blue"
    ).add_to(m)
    print(type(choropleth.geojson))
    print(type(choropleth.color_scale))
    # 地図をhtml形式で出力
    LayerControl().add_to(m)
    m.save(outfile="choropleth_map.html")

if __name__ == "__main__":
    main()