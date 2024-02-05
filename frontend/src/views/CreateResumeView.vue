
<template>
    <div class="container mx-auto">
        <form v-on:submit.prevent="SubmitForm" class="p-5">
            <div class="form-group mb-2">
                <label for="linkedin">Linked in Link</label>
                <input type="text" class="form-control" placeholder="https://www.linkedin.com/in/name" v-model="form.linkedin_link">
            </div>
            <div class="form-group mb-2">
                <label for="summary">Summary</label>
                <textarea class="form-control" rows="5" placeholder="Summary" v-model="form.summary"></textarea>
            </div>

            <button class="btn btn-outline-dark mt-2" type="submit">Submit</button>
        </form>
    </div>
    
</template>

<script>
import axios from 'axios';


export default {
    data(){
        return{
            form:{
                linkedin_link: '',
                summary:'',
            }
        }
    },
 
  
    methods: {
        
        SubmitForm(){
            axios
            .post('/api/resume/', this.form)
            .then(response =>{
                response = 'success';
                alert(response);
                this.$router.push({ name:'home' });
            }) 
            .catch(error => {
                console.log(error)
                
            })
        }
    }

    
}
</script>