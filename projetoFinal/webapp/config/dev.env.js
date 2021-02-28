'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  APP_NAME: '"10 em BD"',
  API_PATH: '"http://34.123.117.26:8000"'
})
