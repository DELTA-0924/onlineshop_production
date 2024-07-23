/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      screens: {
        'xs': {'max': '375px'},
        'xs1': {'max': '370px'},
        'xs2': {'max': '400px'},
      }
    },
  },
  plugins: [],
}