<script setup>
    import Message from "./Message.vue"
</script>

<template>
    <div class="row">
        <div class="container mx-auto d-flex align-items-center justify-content-center">
        
            <form v-on:submit.prevent="submitForm" class="register p-4 shadow bg-body-tertiary rounded w-100" >
                <h1>Register</h1>
                <message :error="error" :success="success" />
                
                <div class="mb-3 row">
                    <label class="col-sm-3" for="">First Name</label>
                    <div class="col-sm-9">
                        <input class="form-control" type="text" v-model="form.first_name" required>
                    </div>
                    
                </div>
                <div class="mb-3 row">
                    <label class="col-sm-3" for="">Last Name</label>
                    <div class="col-sm-9">
                        <input class="form-control" type="text" v-model="form.last_name" required>
                    </div>
                    
                </div>
                <div class="mb-3 row">
                    <label class="col-sm-3" for="">Username</label>
                    <div class="col-sm-9">
                        <input class="form-control" placeholder="username" type="text" v-model="form.username" required>
                    </div>
                </div>
                <div class="mb-3 row">
                    <label class="col-sm-3" for="">Email</label>
                    <div class="col-sm-9">
                        <input class="form-control" placeholder="user@gmail.com" type="email" v-model="form.email" required>
                        <span class="form-text">
                            We'll never share this email to any one.
                        </span>
                    </div>
                    
                </div>
                <div class="password d-flex">
                    <div class="col-md-6 p-1">
                        <label for="">Password</label>
                        <input class="form-control" type="password" placeholder="**********" v-model="form.password" required>
                    </div>
                    <div class="col-md-6 p-1">
                        <label for="">Confirm</label>
                        <input class="form-control" type="password" placeholder="**********" v-model="form.c_password" required>
                    </div>
                </div>
                <div class="mb-3 row">
                    <div class="form-text">
                        Your password must be 8-16 characters long, contain letters and numbers, and must not contain spaces, or emoji.
                    </div>
                </div>
                
                                    
                <button class="mt-2 btn btn-dark" type="submit">Register</button>
                
            </form>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios';


export default {
    components: {
        Message,
    },
    data(){
        return{
        
            error: null,
            success: null,
            form:{
                first_name:'',
                last_name: '',
                username:'',
                password:'',
                c_password:'',
                email:''
            }
        }
    },
    methods:{
        submitForm(){
            this.error = null;
            if (this.form.password != this.form.c_password){
                this.error = 'Password did not match'
            }
            else if (this.form.password.length < 8 || this.form.password.length > 16){
                this.error = 'Password should be at least 8 to 16 characters'
            }
            else{
                axios
                .post('/api/user/', this.form)
                .then(response =>{
                    
                    if (response.data.error){
                        this.error = response.data.error
                    }
                    else{
                        alert('success')
                        this.$router.push({ name:'login' });
                    }                   
                    
                })
                .catch(error =>{
                    console.log(error)

                })
            }
            
            
            
        }
    }

}

</script>