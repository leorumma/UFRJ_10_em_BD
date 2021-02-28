const axios = require('axios')

export const API_PATH = process.env.API_PATH

function req (args) {
  axios({
    url: args.url,
    method: args.method,
    headers: args.header,
    data: args.data,
    params: args.params
  })
    .then(response => {
      if (args.success) {
        console.log(args.method + ' - ' + args.url)
        console.log(args)
        console.log(response)

        args.success(response.data)
      }
    })
    .catch(e => {
      console.log(args.method + ' - ' + args.url)
      console.log(args)
      console.log(e.response)

      args.error(e.response.data.error)
    })
}

export function get (args) {
  args.method = 'get'
  req(args)
}
