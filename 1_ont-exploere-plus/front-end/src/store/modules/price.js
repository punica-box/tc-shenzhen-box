import axios from 'axios'
import * as types from "../mutation-type"

export default {
  state: {
    Price : {
        ont: {
            CN: '',
            EN: ''
        },
        ong: {
            CN: '',
            EN: ''
        },
    }
  },
  mutations: {
    [types.SET_PRICE](state, payload) {
      state.Price = payload.info
    }
  },
  actions: {
    getPrice({dispatch, commit}, $param) {
       
        const price_api_url = (symbol) => {
            let id;
            if(symbol === 'ONT') {
                id = '2566'
            } else if (symbol === 'ONG') {
                id = '3217'
            }
            return `https://api.coinmarketcap.com/v2/ticker/${id}/?convert=CNY`;
        } 
        
        const get_price = (res, lang='EN') => res.data.data.quotes[lang].price.toFixed(2)

        return axios.get(price_api_url('ONT')).then(res => {


                let ont_price = {
                    'CN':  get_price(res,'USD'),
                    'EN':  get_price(res,'CNY')
                } 
            
              axios.get(price_api_url('ONG')).then(res => {

                let ong_price = {
                    'CN':  get_price(res,'USD'),
                    'EN':  get_price(res,'CNY')
                } 
                
                commit({
                    type: types.SET_PRICE,
                    info: {
                        ont: ont_price,
                        ong: ong_price
                    }
                  })
        
            }).catch(error => {
                console.log(error)
              })
    
        }).catch(error => {
            console.log(error)
          })
    }
  }
}
