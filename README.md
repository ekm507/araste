[English Version](./README_EN.md)

<div align="center">
  <h1> آراسته </h1>
  <h2> تبدیل نوشته‌های فارسی به هنر اسکی </h2>

![Untitled](https://github.com/nimafanniasl/araste/assets/76901932/bcaa04fa-318f-4ee8-9b79-d2cc5cc79bbb)


</div>


مشابه ابزار figlet ولی برای نوشته‌های فارسی و عربی


در حال حاضر می‌توانید با دستور زیر، با استفاده از قلمی که تنظیم شده است یک واژه، جمله یا چند سطر نوشته را بنویسید.  

```bash
araste ‌نوشته
```
یا اگر قلمی مدنظر دارید :
```bash
araste 'نوشته‌ی شما' -f 'اسم یا مسیر قلم'
```

برای دیدن فهرستی از قلم‌های نصب‌ شده:

```bash
araste --list
```

درحال‌حاضر چند قلم پیش فرض برای آراسته طراحی شده است که می‌توانید با اسم‌های زیر از آن‌ها استفاده کنید:
<details>
  <summary>aipara</summary>
  <img src="https://github.com/nimafanniasl/araste/assets/76901932/b9812842-bebf-42c6-afcf-a1709af8953c">
</details>

<details>
  <summary>aipara_mini</summary>
  <img src="https://github.com/nimafanniasl/araste/assets/76901932/920187e9-c033-48a8-8975-92a2dd9bb3e8">
</details>
<details>
  <summary>zivar</summary>
  <img src="https://github.com/nimafanniasl/araste/assets/76901932/62f15389-beb5-4432-8d8d-c7e9be9d7c9d">
</details>
<details>
  <summary>nima</summary>
  <img src="https://github.com/nimafanniasl/araste/assets/76901932/f13c09d6-eebc-44eb-8fd0-68160f56e846">

</details>

برای تعیین جهت چینش متن از سوییچ ‪`-a`‬ استفاده کنید.

به‌منظور تعیین پهنای متن چاپ شده از سوییچ ‪`-w`‬ استفاده کنید. آراسته به‌طور پیش‌فرض از پهنای پایانه استفاده می‌کند و درصورتی که امکان آن نباشد، پهنای پیش‌فرض ۸۰ نویسه را استفاده خواهد کرد.

برای راهنما :
```bash
araste -h
```

هم‌چنین می‌توانید ورودی را از طریق stdin به برنامه بدهید. برای مثال:

```bash
echo 'آراسته' | araste
```

یک نمونه از خروجی برنامه با قلم پیش‌فرض آیپارا :
```
                                      ██████
        ████                ██        ██
  ████                      ██          ██
  ████    ██    ██  ██  ██  ██    ██    ██
    ██████████████████████  ██    ██    ██
                                  ██
                                ██
```

### فیلترها

می‌توانید در خروجی آراسته فیلترهای مختلفی اعمال کنید. برای استفاده از فیلترها از سوییچ ‪`-F`‬ استفاده کنید. سوییچ 

برای مثال برای خروجی رنگی از فیلتر `rainbow` استفاده کنید.

```bash
$ araste 'این نوشته رنگی خواهد بود' -F rainbow
```

مثال دیگر: برای چاپ متن آینه‌شده از فیلترهای `hmirror` و `vmirror` استفاده کنید:

```bash
$ araste 'برعکس' -F hmirror
```

خروجی:

```
                ██                      
          ████    ██                    
██  ██      ██  ████  ██  ██  ██        
██████    ██████████████████████    ██  
    ██                        ██    ██  
██    ██                      ████████  
                                        
```

هم‌چنین می‌توانید فیلترهای مختلف را باهم ترکیب کنید. برای این کار به‌سادگی آن‌ها را پشت سر هم بنویسید. مثال:

```bash
$ araste نوشته -F vrainbow box
```

همچنین سوییچ ‪`--filter-list`‬ فهرست فیلترهای موجود را چاپ می‌کند.


```bash
$ araste --filter-list
```


## نصب و استفاده

آراسته در [PyPI](https://pypi.org/project/araste/) قرار دارد. برای نصب برنامه از مدیر بستهٔ پایتون استفاده کنید.

````bash
pip install araste
````
توجه: اگر ارور error: externally-managed-environment رو دریافت میکنید، از pipx برای نصب آراسته استفاده کنید (مطمعن باشید بسته python-pipx روی سیستم شما نصب شده باشد):
````bash
pipx install araste
````

یا اگر می‌خواهید خودتان آراسته را بیلد کنید:

```bash
pip install setuptools wheel
git clone 'https://github.com/ekm507/araste/'
cd araste
rm -rf dist
python3 setup.py bdist_wheel
pip install ./dist/*.whl
```

## نصب قلم‌های بیشتر
برای نصب فونت‌ها می‌توانید از araste-get استفاده کنید.
````bash
araste-get install FontName
````
[قلم های قابل نصب](https://github.com/ekm507/araste-fonts/blob/main/Fonts.md)

## حذف برنامه
برای پاک کردن برنامه از روی سیستم، می‌توانید از pip استفاده کنید.

````bash
pip uninstall araste
````
یا با استفاده از pipx.

````bash
pipx uninstall araste
````
## ساخت قلم

برای دریافت قلم‌های بیشتر و هم‌چنین ساخت قلم خودتان از مخزن [araste-fonts](https://github.com/ekm507/araste-fonts) استفاده کنید.  
در آن مخزن قلم‌های ساخته شده و افزوده شده توسط کاربران، راهنماهایی برای ساخت طراحی و ساخت قلم و همچنین ابزارهای مختلفی برای این منظور وجود دارد.

## برای انجام
برای انجام کار جدید فایل [TODOS.md](https://github.com/ekm507/araste/blob/main/TODOS.md) را مشاهده کنید
