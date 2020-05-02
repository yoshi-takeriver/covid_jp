# covid_jp

東京都におけるCOVID-19についての各種データを行政区別にビジュアライズする

## 参考

[python folium で、都内の公園にまつわる情報を地図上に描画する](https://www.monotalk.xyz/blog/python-folium-%E3%81%A7%E9%83%BD%E5%86%85%E3%81%AE%E5%85%AC%E5%9C%92%E3%81%AB%E3%81%BE%E3%81%A4%E3%82%8F%E3%82%8B%E6%83%85%E5%A0%B1%E3%82%92%E5%9C%B0%E5%9B%B3%E4%B8%8A%E3%81%AB%E6%8F%8F%E7%94%BB%E3%81%99%E3%82%8B/)

参考
folium: official github
<https://github.com/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb>  
<https://python-visualization.github.io/folium/quickstart.html#Getting-Started>  
python folium で、都内の公園にまつわる情報を地図上に描画する
<https://www.monotalk.xyz/blog/python-folium-%E3%81%A7%E9%83%BD%E5%86%85%E3%81%AE%E5%85%AC%E5%9C%92%E3%81%AB%E3%81%BE%E3%81%A4%E3%82%8F%E3%82%8B%E6%83%85%E5%A0%B1%E3%82%92%E5%9C%B0%E5%9B%B3%E4%B8%8A%E3%81%AB%E6%8F%8F%E7%94%BB%E3%81%99%E3%82%8B/>  
Qiita: Folium: Pythonでデータを地図上に可視化
<https://qiita.com/nanakenashi/items/824c0cb16860ca59a424>  
Folium: Python で地図可視化
<https://takaishikawa42.hatenablog.com/entry/2019/01/11/234716>  

Folium: error
<https://github.com/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb>

## 現状

とりあえず今はfolium 0.8.3 + tokyo23.jsonを組み合わせている（plot_map.py）

### foliumについて

foliumの動作はgeojsonの形式に大きく依存するらしい  

| -             | us-state.json | tokyo23.json | tokyo.json |
| ------------- | :-----------: | :----------: | :--------: |
| folium 0.10.1 |      〇       |      ×\*       |     ×\*      |
| folium 0.8.3  |      〇       |      〇      |     ×      |

\*: 動きはするが、地図上（カラー）に値は反映されず、すべてにnanが入っていた（nan_fill_colorで確認）

issue: <https://github.com/python-visualization/folium/issues/1045>によると、<https://nbviewer.jupyter.org/github/python-visualization/folium/blob/e26d044bbcb911ba16809154aeb0f611636ab11d/examples/plugin-Search.ipynb>のようにgeopandasを使って値をマージしろと書いてある  

同様の記述が<https://github.com/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb>にある

### scraping



## 今後