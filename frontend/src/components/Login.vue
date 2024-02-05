<script setup>
    import Message from "./Message.vue"
</script>

<template>
    <div class="row">
        <div class="container mx-auto d-flex align-items-center justify-content-center">
            <form v-on:submit.prevent="submitForm" class="login p-4 shadow bg-body-tertiary rounded w-100">
                <h1>Login</h1>
                <message :error="error" :success="success" />
                <div class="mb-3">
                    <label for="">Username</label><br/>
                    <input type="text" class="form-control" placeholder="Username" v-model="form.username" required/>
                </div>
                <div class="mb-3">
                    <label for="">Password</label><br/>
                    <input type="password" class="form-control"  placeholder="Password" v-model="form.password" required/>
                </div>
                
                
                <button type="submit" class="mt-2 btn btn-dark">Login</button><br />
            </form>
        </div>
        
    </div>
</template>

<script>
import store from '@/store';

console.log(store.getters.isAuthenticated)
export default {
    data(){
        return {
            success: null,
            error: null,
            form:{
                username: '',
                password: '',
            }
        }
    },
    methods:{
        async submitForm(){
            this.error = null;
            
            store.commit('setError', null);
            await store.dispatch('submitForm', this.form);
            
            if (store.getters.isAuthenticated) {
                this.$router.push({ name:'home' });
                console.log(store.getters.isAuthenticated)
            }
            if (store.getters.error){
                this.error = store.getters.error
            }
            
        }
    }
}

</script>
