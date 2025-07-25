import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        darkblue: {
          50: '#e6ecf8',
          100: '#ccd9f0',
          200: '#99b3e1',
          300: '#668cd2',
          400: '#3366c3',
          500: '#0033b3',
          600: '#002b97',
          700: '#00227a',
          800: '#001a5e',
          900: '#001341',
          950: '#000d29'
        }
      }
    }
  },
  plugins: []
}

export default config
