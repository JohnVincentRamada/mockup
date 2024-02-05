<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <div class="container">

        <div v-if="resumes.length === 0" class="d-flex align-items-center justify-content-center">
            <RouterLink to="/createresume" class="mx-2">
                <button class="btn btn-outline-dark">
                    Create Resume
                </button>
            </RouterLink>
            <small>not yet configured</small>
        </div>

        <div v-else class="container">
            <div class="d-flex align-items-center justify-content-between">
                <div class="profile-detail">
                    <div v-for="account in accounts" v-bind:key="account.id">
                        <h2>{{ account.first_name }} {{ account.last_name }}</h2>
                        <p v-for="detail in details" v-bind:key="detail.id">{{ detail.address }}</p>
                    </div>
                    <div class="row" v-for="detail in details" v-bind:key="detail.id">
                        <div class="col-md-10">
                            <p v-for="account in accounts" v-bind:key="account.id">{{ account.email }}</p>
                            <p v-for="resume in resumes" v-bind:key="resume.id"><a :href="'https://' + resume.linkedin_link" class="link-underline link-underline-opacity-0">{{ resume.linkedin_link }}</a></p>
                        </div>
                        <div class="col-md-2">
                            <p>{{ detail.contact_number }}</p>
                        </div>
                    </div>
                </div>
                <div v-for="detail in details" v-bind:key="detail.id">
                    <img v-bind:src="axios.defaults.baseURL + detail.profile_picture" v-bind:alt="detail.profile_picture" class="image">
                </div>   
            </div>
            
            <div class="summary">
                <div class="title d-flex">
                    <h4 class=" fw-bold">Summary </h4>
                    <RouterLink to="/updatesummary"><font-awesome-icon icon="fa-solid fa-pen-to-square" /></RouterLink>
                </div>
                
                <div v-for="resume in resumes" v-bind:key="resume.id">
                    <p>{{ resume.summary }}</p>
                </div>
            </div>

            <div class="education">
                <div class="title d-flex">
                    <h4 class="fw-bold">Education</h4>
                    <RouterLink to="/addeducation"><font-awesome-icon icon="fa-solid fa-file-circle-plus" /></RouterLink>
                </div>
                <div v-for="education in educations" v-bind:key="education.id">
                    <div class="d-flex">
                        <div class="p-2">
                            <img v-bind:src="axios.defaults.baseURL + education.image" v-bind:alt="education.image" class="image-logo">
                        </div>
                        <div class="p-2">
                            
                            <h5>{{ education.school }}</h5>
                            <p>{{ education.degree }}</p>
                            <p>{{ education.year_started }} - {{ education.year_ended }}</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="reward">
                <div class="title d-flex">
                    <h4 class="fw-bold">Honors and Rewards</h4>
                    <RouterLink to="/addreward"><font-awesome-icon icon="fa-solid fa-file-circle-plus" /></RouterLink>
                </div>
                <div v-for="reward in rewards" v-bind:key="reward.id">
                    <div class="d-flex">
                        <div class="p-2">
                            <img v-bind:src="axios.defaults.baseURL + reward.image" v-bind:alt="reward.image" class="image-logo">
                        </div>
                        <div class="p-2">
                            
                            <h5>{{ reward.award }} - {{ reward.organization }}</h5>
                            <p>{{ reward.issued }}</p>
                            <p>{{ reward.description }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    
    

    
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return{
            resumes: [],
            educations: [],
            rewards: [],
            accounts: [],
            details: [],            
        }
    },
 
    mounted(){
        this.getDetails();
        this.getAccounts();
        this.getResumeLists()
        this.getEducationLists()
        this.getHonorsAndRewardsLists()
    },
    methods: {
        
        
        getResumeLists(){
            axios
            .get('/api/resume/')
            .then(response =>{
                
                this.resumes = response.data
            }) 
            .catch(error => {
                console.log(error)
                
            })
        },
        getEducationLists(){
            axios
            .get('/api/education/')
            .then(response =>{
                
                this.educations = response.data
            }) 
            .catch(error => {
                console.log(error)
                
            })
        },
        getHonorsAndRewardsLists(){
            axios
            .get('/api/honorawards/')
            .then(response =>{
                
                this.rewards = response.data
            }) 
            .catch(error => {
                console.log(error)
                
            })
        },
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