import { endAnimation } from '../../../../features/components/main/loadAnimation.js'
import { Form } from './../../../forms/form.js'


document.addEventListener('DOMContentLoaded', () => {endAnimation()})
document.addEventListener('DOMContentLoaded', makeValidation)


function makeValidation() {

    let fieldsObj = {

        stringFields: [
            ['email', []],
        ]

    }


    let form = new Form('form', fieldsObj)
    form.addEvents()
}