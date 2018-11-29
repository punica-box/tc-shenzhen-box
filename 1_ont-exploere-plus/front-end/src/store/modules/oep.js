import axios from 'axios'
import * as types from "../mutation-type"

export default {
  state: {
    history : [],
    detail:'',
    list:[]
  },
  mutations: {
    [types.SET_OEP_TOKEN_LIST](state, payload) {
      state.list = payload.info
    },
    [types.SET_OEP_TOKEN_HISTORY](state, payload) {
      state.history = payload.info
    },
    [types.SET_OEP_TOKEN_DETAIL](state, payload) {
      state.detail = payload.info
    }
  },
  actions: {
      getOepTokenList({dispatch, commit}, $param) {
        
        return axios.get('/oep4token/list').then(res => {

            console.log(res.data)

            commit({
                type: types.SET_OEP_TOKEN_LIST,
                info: res.data
              })
    
        }).catch(error => {
            console.log(error)
          })
    },
    getOepTokenDetail({dispatch, commit}, $param) {
       
        const oep_token_detail_api_url = (contractAddr) => {
            return `/oep4token/detail/${contractAddr}`;
        } 
        
        return axios.get(oep_token_detail_api_url($param.contractAddr)).then(res => {

            console.log(res.data)

            commit({
                type: types.SET_OEP_TOKEN_DETAIL,
                info: res.data
              })
    
        }).catch(error => {
            console.log(error)
          })
    },
    getOepTokenHistory({dispatch, commit}, $param) {
       
        const oep_token_history_api_url = (contractAddr) => {
            return `/oep4token/${contractAddr}`;
        } 
        
        return axios.get(oep_token_history_api_url($param.contractAddr)).then(res => {

            console.log(res.data)

            commit({
                type: types.SET_OEP_TOKEN_HISTORY,
                info: res.data
              })
    
        }).catch(error => {
            console.log(error)
          })
    }
  }
}
