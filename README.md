# 雪盈证券 Open API Python SDK 接入说明书

## 接入准备

### 开户入金

开发者在接入雪盈证券开发平台之前，需要提前开通雪盈账号。账号开通后，您可以自己的账号ID（以后统称为：account id）作为您账号的唯一标识。

#### 开户地址

[开户链接](https://www.snowballsecurities.com/xy-account-open/phone-verify)

> `https://www.snowballsecurities.com/xy-account-open/phone-verify`

#### 查看账户 ID

登录雪盈证券APP，查找“我的-设置-账号与安全”，即可看到雪盈账号 ID。

### 申请密钥

获取自己的 accountId 后可以在雪盈官网-申请 API，来注册开发者信息，注册后将获得您自己的专属密钥（以后统称为：secret key）作为您登录雪盈开发平台的唯一凭证，请妥善保存。

[注册地址](https://www.snowballsecurities.com)

> `https://www.snowballsecurities.com`

### 引入代码

获取 secret key 后即可进行 Python SDK 接入，有以下几种获取 SDK 的方式：

#### pip 安装

##### 测试仓库

`pip install -i https://test.pypi.org/simple/ snbpy==1.0.0`

##### 正式仓库(暂未发布)

`pip install snbpy`

#### 源码安装

[源码仓库](https://github.com/snowballsecurities/snbpy)

> `https://github.com/snowballsecurities/snbpy`

`python3 setup.py install`

> 请与客户经理联系获取源码或者访问项目 GitHub 首页获取

### 环境说明

雪盈证券为 API 开发者提供两套环境，分别是 sit 测试环境和 prod 生产环境，现对这两套环境做分别说明。

| **环境** | **环境名称** | **链接方式**                             | **账号获取**     |
| -------- | ------------ | ---------------------------------------- | ---------------- |
| sit      | 测试环境     | `https://sandbox.snbsecurities.com` | 联系雪盈客服获得 |
| prod     | 正式环境     | `https:// openapi.snbsecurities.com` | 参考1.1和1.2     |

>  **PORD**  环境中用户账号、资金均为真实账号、资金，所做操作全部真实有效，请**勿**做测试操作。

> SIT 环境的用户账户为模拟账号，资金是虚拟的用于测试验证，测试账号的申请联系雪盈证券 API 服务群的群主。

## 快速开始

### 代码概要

SDK 主要有以下几个类 

* SnbConfig SDK 的 Client 的基础配置
  > `from snbpy.common.domain.snb_config import SnbConfig`
* TradeInterface API 的 接口类,包含 10 个抽象方法,对应 10 种 API.
* SnbApiClient SDK 的基础框架.
  > `from snbpy.snb_api_client import SnbHttpClient, TradeInterface`

### 配置项

| **key**    | **含义**        | **备注** |
| ---------- | --------------- | -------- |
| account    | U 账户          |          |
| key        | API access Key  |          |
| sign_type  | 加密方式        | 暂不支持 |
| snb_server | API 服务器地址  |          |
| snb_port   | API 服务器端口  |          |
| timeout    | Http 超时时间   |          |
| cache_path | 缓存路径        | 暂不支持 |
| schema     | API Http Schema |          |
| auto_login | 是否自动登陆    | 暂不支持 |

### 调用示例

SDK 提供了Http API 的 requests 实现 `SnbHttpClient(SnbApiClient)`, 如想替换其他 httpClient 可以重写 `_do_execute` 方法, 下面是登陆并查询订单的示例代码. 

```python
from snbpy.common.domain.snb_config import SnbConfig
from snbpy.snb_api_client import SnbHttpClient
if __name__ == '__main__':
    config = SnbConfig()
    config.account = "DU876752"
    config.key = '123456'
    config.sign_type = 'None'
    config.snb_server ='sandbox.snbsecurities.com'
    config.snb_port = '443'
    config.timeout = 1000
    config.schema = 'https'

    client = SnbHttpClient(config)
    client.login()
    order_list_response = client.get_order_list()
```



### 管理

token是一串无序加密的字符串，形如: `pwQxtqj3Bl1q3ThX3I5rRJyUyQxffWX9`，在访问 API 时，用户需携带该 token 作为身份凭证。用户获取 token 的个数没有限制，但服务器仅为每个用户保存 10 个有效 token ，再用户连续申请第 11 个 token 时，第一个 token 开始失效，以此类推。

`SnbHttpClient` 中封装了token相关的方法，login 方法会直接访问API获取一个Auth对象，包含了token和过期时间.

### 方法描述

更多详情请使用 `help(TradeInterface)` 方法获取文档

```python
>>> from snbpy.snb_api_client import TradeInterface
>>> help(TradeInterface)
```

以下是方法列表

| 方法名               | 描述                                   |
| -------------------- | -------------------------------------- |
| login                | 访问API生成一个新token，不会使用缓存   |
| get_token_status     | 查询token，一般用于查询token的过期时间 |
| place_order          | 下单                                   |
| get_order_by_id      | 订单查询，单条                         |
| get_order_list       | 订单查询，批量                         |
| cancel_order         | 撤销订单                               |
| get_position_list    | 持仓查询                               |
| get_balance          | 资产查询                               |
| get_security_detail  | 证券信息查询                           |
| get_transaction_list | 成交查询                               |

## 数据字典

### Currency

| 名称 | 描述         |
| ---- | ------------ |
| BASE | 基础货币     |
| USX  |              |
| CNY  | 人民币       |
| USD  | 美元         |
| SEK  | 瑞典克朗     |
| SGD  | 新加坡币     |
| TRY  | 土耳其里拉   |
| ZAR  | 南非兰特     |
| JPY  | 日元         |
| AUD  | 澳元         |
| CAD  | 加币         |
| CHF  | 瑞士法郎     |
| CNH  | 人民币       |
| HKD  | 港币         |
| NZD  | 新西兰币     |
| CZK  | 捷克克朗     |
| DKK  | 丹麦克朗     |
| HUF  | 匈牙利福林   |
| NOK  | 挪威克朗     |
| PLN  | 波兰兹罗提   |
| EUR  | 欧元         |
| GBP  | 英镑         |
| ILS  | 以色列谢克尔 |
| MXN  | 墨西哥比索   |
| RUB  | 卢布         |
| KRW  | 韩元         |

### SecurityType

| 名称  | 描述               |
| ----- | ------------------ |
| STK   | 股票               |
| FUT   | 期货               |
| OPT   | 期权               |
| FOP   | 期货期权           |
| WAR   | 涡轮               |
| MLEG  | 不支持             |
| CASH  | 外汇               |
| CFD   | 差价合约           |
| CMDTY | 大宗商品           |
| FUND  | 基金               |
| IOPT  | 牛熊证             |
| BOND  | 债券               |
| ALL   | 全部类型(查询条件) |

### OderType

| 名称              | 描述       |
| ----------------- | ---------- |
| LIMIT             | 限价单     |
| MARKET            | 市价单     |
| AT                | 不支持     |
| ATL               | 不支持     |
| SSL               | 不支持     |
| SEL               | 不支持     |
| STOP              | 止损单     |
| STOP_LIMIT        | 限价止损单 |
| TRAIL             | 追踪单     |
| TRAIL_LIMIT       | 限价追踪单 |
| LIMIT_ON_OPENING  | 开市限价单 |
| MARKET_ON_OPENING | 开市市价单 |
| LIMIT_ON_CLOSE    | 闭市限价单 |
| MARKET_ON_CLOSE   | 闭市市价单 |

### OrderSide

| 名称 | 描述 |
| ---- | ---- |
| BUY  | 买入 |
| SELL | 卖出 |

### OrderStatus

| 名称               | 描述     |
| ------------------ | -------- |
| NO_REPORT          | 未报     |
| WAIT_REPORT        | 待报     |
| REPORTED           | 已报     |
| WAIT_WITHDRAW      | 已报待撤 |
| PART_WAIT_WITHDRAW | 部成待撤 |
| PART_WITHDRAW      | 部撤     |
| WITHDRAWED         | 已撤     |
| PART_CONCLUDED     | 部成     |
| CONCLUDED          | 已成     |
| INVALID            | 废单     |

### TimeInForce

| 名称 | 描述       |
| ---- | ---------- |
| DAY  | 当日有效   |
| GTC  | 撤单前有效 |

## 更新日志

| 更新日期   | 更新内容                         |version|
| ---------- | -------------------------------- |---|
| 2020-11-24 | 增加更多日志, 增加 OrderID 的非空验证 |1.0.1|
| 2020-07-08 | 更新至当前最新安装方式与连接方式 | 1.0.0|
| 2020-06-08 | 初始化更新                       |--|

##  **联系我们**

如果您在使用过程中遇到任何问题，可以通过以下方式联系我们获取帮助，雪盈证券客服电话：400-118-8886。

