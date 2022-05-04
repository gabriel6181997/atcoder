# atcoder
[こちら](https://qiita.com/KoyanagiHitoshi/items/32dc42d8c5ee75339e54#%E7%AC%AC1%E7%AB%A0-%E5%85%A5%E5%87%BA%E5%8A%9B%E5%87%A6%E7%90%86%E8%A6%B3%E7%82%B9)の記事の順番の通り、問題を解答中。

## 問題文をコピペするのに使うコード
```
(() => {
  let str = "# -*- coding: utf-8 -*-\n'''\n";
  str +=
    document
      .querySelector("#main-container span.h2")
      .textContent.replace("解説", "")
      .trim() + "\n";
  document
    .querySelectorAll("#main-container div.part > section")
    .forEach((item) => {
      str += item.textContent.trim() + "\n";
    });
  console.log(str + "'''");
})();
```

### まだ解いていない問題リスト
・　[キーエンス プログラミング コンテスト 2020 C - Subarray Sum](https://atcoder.jp/contests/keyence2020/tasks/keyence2020_c?lang=ja)
