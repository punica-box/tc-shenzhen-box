<template>

        <div class="container margin-top-60">
        <div class="pc-display">

            <return-home></return-home>
            <list-title :name="tokenDetail.symbol">

            </list-title>

            <p>OEP4 代币名称：{{tokenDetail.name}}</p>
            <p>合约地址：{{contractAddress}}</p>
            <p>总供应量：{{tokenDetail.total_supply}}</p>

            <div class="row font-size14" v-for="h in tokenHistory">
                <div class="col">
                <div class="detail-col trans-tx-col">
                    <div class="row">
                        <div @click="toAddressPage(h.from_addr)" class="col pointer">{{h.from_addr}}</div>
                        <div class="col">>></div>
                        <div class="col-4 text-center font-weight-bold font-size18">{{ h.trans_amount + ' '+ tokenDetail.symbol }} 
                        </div>
                        <div class="col text-right">>></div>
                        <div @click="toAddressPage(h.to_addr)" class="col text-right pointer">{{h.to_addr}}</div>
                    </div>
                     <div class="row">
                        <div class="col text-right">{{ toDatetime(h.timestamp) }}</div>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </div>

        
</template>

<script>
import {mapState, mapGetters} from 'vuex'

export default {
    name: "oep-token",
    data() {
        return {
            contractAddress:''
        }
    },
    created() {
        this.contractAddress = this.$route.params.contractAddress;
    },
    mounted() {
        this.getOepTokenHistory()
        this.getOepTokenDetail()
    },
    computed: {
      ...mapState({
        tokenDetail: state => state.Oep.detail,
        tokenHistory: state => state.Oep.history
      })
    },
    methods: {

        getOepTokenDetail() {
            this.$store.dispatch('getOepTokenDetail', {'contractAddr':this.contractAddress}).then()
        },
        getOepTokenHistory() {
            this.$store.dispatch('getOepTokenHistory', {'contractAddr':this.contractAddress}).then()
        },
        toDatetime(timestamp) {
            let unixTimestamp = new Date(timestamp * 1000) 
            let commonTime = unixTimestamp.toLocaleString()
            return commonTime;
        },
        timeStamp2String (time){
           let datetime = new Date();
             datetime.setTime(time);
            let year = datetime.getFullYear();
            let month = datetime.getMonth() + 1;
            let date = datetime.getDate();
            let hour = datetime.getHours();
            let minute = datetime.getMinutes();
            let second = datetime.getSeconds();
            let mseconds = datetime.getMilliseconds();
            return year + "-" + month + "-" + date+" "+hour+":"+minute+":"+second+"."+mseconds;
        },
        toAddressPage(address) {
            this.$router.push({name: 'AddressDetail', params: {address: address, pageSize: 20, pageNumber: 1}})
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
