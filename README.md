# CHI TIẾT API

1. [Đăng nhập](README.md#đăng-nhập)
2. [Lấy tất cả tên Box](README.md#lấy-tất-cả-tên-box)
3. [Lấy thông tin Box](README.md#lấy-thông-tin-box)

## Đăng nhập

Phương thức: `GET`

Route: `/login`

Return:

```json
{
    "account_address": "7SBJ7GJKFJHXHGQU3G23U552NJZY5AQZO7NNVY76DFMDLWUPWZEIWH3NPQ"
}
```

## Lấy tất cả tên Box

Phương thức: `GET`

Route: `/getAllBox`

Return:

```json
{
    "application-id": 680721238,
    "boxes": [
        {
            "name": "boxA"
        },
        {
            "name": "boxB"
        }
    ],
    "next-token": "b64:Ym94Qg=="
}
```

## Lấy thông tin Box

Phương thức: `GET`

Route: `/getDetailsBox`

Params:

- Key: `name`, Value: `boxA`

Return:

```json
{
    "name": "boxA",
    "round": 40936329,
    "value": "hahahahah"
}
```
