/** @type {import('tailwindcss').Config} */

export default {
  content: ["./src/**/*.{html,js,jsx}"],
  theme: {
    extend: {
      backgroundImage: {
        'mg-logo': "url('/mg-logo.png')",
      },
      from: {
        'mg-logo': "url('/mg-logo.png')",
      },
      padding: {
        '2.5': "10.5px",
      },
      colors: {
        'mg-purple': '#5409C2',
        'mg-dark-blue': '#8841BD',
      },
      fontFamily: {
        'poppins': ['Poppins', 'sans-serif'], 
        'jetbrains': ['JetBrains Mono', 'monospace'] // Adiciona a família de fontes JetBrains Mono
      },
    },
  },
  plugins: [],
}
