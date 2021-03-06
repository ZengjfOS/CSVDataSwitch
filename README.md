# CSV Data Switch

## 目录架构

```
    .
    ├── image
    │   └── output.png
    ├── input                      <--------- 将所有的csv文件让入这个文件夹
    │   ├── 16AFFFBB18AA.csv
    │   └── 16B00A4118AA.csv
    ├── main.py                    <--------- 使用Python3运行该程序
    ├── output.csv                 <--------- main.py程序输出文件
    ├── config.ini                 <--------- 参考配置文件
    └── README.md
```


## 使用说明

* 编码语言采用[Python 3](https://www.python.org/)，请安装Python解释器：[Download Python 3](https://www.python.org/downloads/)
* 将所有的[csv](http://baike.baidu.com/item/CSV/10739)文件，放入[input](input)目录；  
* 修改[config.ini](config.ini)文件内容以满足对获取列的内容，配置文件标准请参考：[Configuration file parser](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure)
  * 只需要写**section**部分，其他部分不需要，请参考当前的[config.ini](config.ini)进行修改；
  * 目前支持csv文件任意列值与config.ini的section中的值进行匹配，**不可重复**；
    * 支持`valueColumn`属性，表示**section**对应的**value**在哪一列，默认值是1(列号从1开始算)，且要大于等于1；
    * 支持`direction`属性，`"right"`表示`value`在`key`的右侧，`"down"`表示`value`在`key`的下方；
    ```
        [Sensor Serial Number]
        direction = right
        valueColumn = 2
        [number_static_bad_pixels]
        direction = down
        valueColumn = 4
        [number_dynamic_bad_pixels]
        direction = down
        valueColumn = 5
    ```
* 输出文件名：[output.csv](output.csv)；

## 输出信息

![output.csv](image/output.png)
