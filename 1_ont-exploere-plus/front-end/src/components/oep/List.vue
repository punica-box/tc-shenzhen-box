<template>

        <div class="container margin-top-60">
        <div class="pc-display">

            <return-home></return-home>
            <list-title :name="title"></list-title>

            <table class="table table-hover">
                <thead>
                <tr>
                </tr>
                </thead>
                <tbody>
                    <tr v-for="t in tokenList">
                        <td class="td11" style="padding: 34px 24px;">
                            <p @click="toTokenDetailPage(t.smc_addr)" class="font-size24  p_margin_bottom n_color font-Regular pointer">代币代码：{{t.symbol}}</p>
                            <p class="font-size24  p_margin_bottom n_color font-Regular">代币名称：{{t.name}}</p>
                        </td>
                       
                        
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

        
</template>

<script>
import {mapState, mapGetters} from 'vuex'

export default {
    name: "oep-token",
    data() {
        return {
            title:'OEP4 TOKEN 列表'
        }
    },
    mounted() {
        this.getOepTokenList()
    },
    computed: {
      ...mapState({
        tokenList: state => state.Oep.list
      })
    },
    methods: {
        getOepTokenList() {
            this.$store.dispatch('getOepTokenList', {}).then()
        },
        toTokenDetailPage(smc_addr) {
            this.$router.push({name: 'OepToken', params: {contractAddress: smc_addr}})
        }
    }
}

</script>

<style scoped>
  .trans-tx-col {
    background: #32A4BE;
    color: white;
    font-size: 14px;
  }
</style>
