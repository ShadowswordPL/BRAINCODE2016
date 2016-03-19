//
//  DevViewController.swift
//  ClassList
//
//  Created by Tomasz Bąk on 19.03.2016.
//  Copyright © 2016 Za Duzo Tomkow. All rights reserved.
//

import UIKit

class DevViewController: UIViewController {
    static var address: String = "10.3.8.65"
    
    @IBAction func change(sender: UITextField) {
        DevViewController.address = sender.text!
    }
}
