module.exports = {
  content: [
    "./templates/**/*.{html,js}",   // Django 的 HTML 模板
    "./src/**/*.{html,js,ts,jsx,tsx}", // 如果有前端檔案
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}
