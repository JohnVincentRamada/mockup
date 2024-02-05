<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
    <div class="row">
        <div class="container mx-auto d-flex align-items-center justify-content-center">
            <div class="card mb-3 shadow bg-body-tertiary rounded">
                <div class="row g-0">
                    <div v-for="detail in details" v-bind:key="detail.id"  class="col-md-4">
                        <img v-bind:src="axios.defaults.baseURL + detail.profile_picture" v-bind:alt="detail.profile_picture" class="image">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <div v-for="account in accounts" v-bind:key="account.id">
                                <h2 class="text-center mt-2 card-title">{{ account.first_name }} {{ account.last_name }} @{{ account.username }}</h2>
                                <i v-for="account in accounts" class="card-text" >{{ account.email }}</i>
                            </div>
                            <div v-for="detail in details" v-bind:key="detail.id" class="d-flex justify-content-between">
                                <p>{{ detail.contact_number }}</p>
                                <p>{{ detail.address }}</p>
                            </div>
                            
                            <RouterLink to="/updateProfile">
                                <button class="btn btn-outline-dark">Update Profile</button>
                            </RouterLink>
                            
                            
                        </div>
                    </div>
                </div>
            </div>
        </div> 
    </div>

    <div class="row">
        <div class="container">

        </div>
    </div>

    
</template>

<script>
import axios from 'axios'
export default {

    data() {
        return{
            accounts: [],
            details:[],
        }
    },

    mounted(){
        this.getDetails();
        this.getAccounts();
    },
    methods: {
        
        getAccounts(){
            axios
            .get('/api/user/')
            .then(response =>{
                this.accounts = response.data
            })
            .catch(error =>{
                console.log(error)
            })
        },
        getDetails(){
            axios
            .get('/api/userdetail/')
            .then(response =>{
                this.details = response.data
                console.log(response.data.profile_picture)
            })
            .catch(error =>{
                console.log(error)
            })
        }

    }

    

}
</script>