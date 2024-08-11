# nokia_png_generate 

**Fork Form [dcalsky/zzkia](https://github.com/dcalsky/zzkia)**

生成复古的诺基亚短信图片

原作者很久没有更新，并且按照原作者README我的docker开不了(

为python部分api的sanic服务器添加了cors策略(其实就两行T_T)，分开前端和后端的端口以保证可以在同一主机上使用

## Demo picture: 

![](./public/demo.png)

## 开发和部署

> [!NOTE]环境要求
> Python 3.8.4\
> Node >= 20.15.0

### 后端服务器

其在本地3001端口启动

```bash
python api/main.py
```

### 前端Web页面

安装依赖：
```bash
npm install 
```

构建：
```bash
npm run build 
```

启动(访问本地3000端口)：
```bash
npm run start 
```

开发模式：
```bash
npm run dev 
```

更多参数说明和启动入口参见`package.json`和`api/main.py`文件

## TODO

原作者的Dockerfile文件会在不定时间之后出新版本