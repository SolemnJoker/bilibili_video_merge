# 1.简介
此脚本用于将bilbili手机端客户端下载的视频和音频合并。
由于手机客户端下载的视频是视频和音频分开的，所以如果需要放到pc上用第三方播放器播放则需要将视频和音频合并。

# 2.依赖
python
ffmpeg
```
sudo apt install ffmpeg 
```

# 3.用法
## 3.１拷贝手机（安卓）中已下载好的视频
手机下载好的视频在
`手机根目录/Android/data/tv.danmaku.bili/download`目录下
![视频下载目录](https://gitee.com/Solemnjoker/PicGo/raw/master/image/20200605185905.png)

## 运行脚本
如图文件目录如下
![](https://gitee.com/Solemnjoker/PicGo/raw/master/image/20200605190514.png)

```
![](https://gitee.com/Solemnjoker/PicGo/raw/master/image/20200605190911.png)kdjflsk
python ./merge.py ./data/2345456
```
![](https://gitee.com/Solemnjoker/PicGo/raw/master/image/20200605190911.png)
则会将2345456目录下的多个分p的视频音频都分别合并，并根据b站中视频名字重命名文件名






