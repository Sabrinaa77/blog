/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",   // Django 模板
    "./**/*.py",               // 如果 Python 中有寫 className
    "./static/**/*.js",        // 你的前端 js
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),        // 如果不用 DaisyUI 可以刪掉這行
  ],
}
